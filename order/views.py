import requests
import json
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags
from django.http import HttpResponse, JsonResponse
from .models import Order, OrderItem, BankAccount
from .forms import OrderCreateForm, PaystackPaymentForm
from cart.models import Cart, CartItem
from core.models import SiteSettings


def send_order_confirmation_email(order):
    site_settings = SiteSettings.objects.first()
    subject = f"Order Confirmation - {order.id}"
    to_email = [order.email]
    from_email = settings.EMAIL_HOST_USER
    admin_email = settings.ADMIN_EMAIL  # Ensure ADMIN_EMAIL is correctly defined in settings

    context = {
        'order': order,
        'site_settings': site_settings,
    }

    message_user = render_to_string('emails/order_confirmation.html', context)
    message_admin = render_to_string('emails/order_confirmation_admin.html', context)

    # Send email to user
    send_mail(subject, strip_tags(message_user), from_email, to_email, html_message=message_user)

    # Send email to admin
    send_mail(subject, strip_tags(message_admin), from_email, [admin_email], html_message=message_admin)


@login_required
def order_create(request):
    cart = get_object_or_404(Cart, user=request.user)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.created_at = timezone.now()
            order.save()  # Save the order to generate an ID
            # Now that the order is saved, you can generate the payment reference
            order.payment_reference = f"DT-{order.id}-{timezone.now().strftime('%Y%m%d%H%M%S')}"
            order.save()  # Save the order again to update the payment reference
            for item in cart.items.all():
                OrderItem.objects.create(order=order, menu_item=item.menu_item, price=item.menu_item.price, quantity=item.quantity)
            cart.items.all().delete()
            send_order_confirmation_email(order)  # Send order confirmation email
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderCreateForm()
    return render(request, 'order/order_create.html', {'cart': cart, 'form': form})


def send_order_status_update_email(order):
    site_settings = SiteSettings.objects.first()  # Adjust query as needed

    subject = f"Order Status Update - {order.id}"
    to_email = [order.email]
    from_email = settings.EMAIL_HOST_USER

    context = {
        'order': order,
        'site_settings': site_settings,
    }

    message = render_to_string('emails/order_status_update.html', context)

    send_mail(subject, message, from_email, to_email, html_message=message)

# Call this function whenever the order status is updated
def update_order_status(order, new_status):
    order.status = new_status
    order.save()
    send_order_status_update_email(order)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/order_detail.html', {'order': order})


@login_required
def payments_select(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'order/payments.html', {
        'order': order,
    })


@login_required
def paystack_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        email = order.email
        amount = int(order.get_total_cost())  # Ensure this returns the amount in your desired currency

        headers = {
            'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
            'Content-Type': 'application/json',
        }
        data = {
            'email': email,
            'amount': amount * 100,  # Paystack expects amount in kobo
        }
        try:
            response = requests.post('https://api.paystack.co/transaction/initialize', headers=headers, json=data)
            if response.status_code == 200:
                response_data = response.json()
                authorization_url = response_data['data']['authorization_url']
                paystack_reference = response_data['data']['reference']
                order.pystk_ref = paystack_reference
                order.save()

                return redirect(authorization_url)
            else:
                # Handle Paystack API error response
                pass
        except requests.RequestException as e:
            # Handle exceptions (e.g., connection error)
            pass

    context = {
        'order': order,
        'email': order.email,
        'amount': int(order.get_total_cost()),
        'first_name': order.first_name,
        'last_name': order.last_name,
    }
    return render(request, 'order/paystack_payment.html', context)
    

@login_required
def direct_transfer_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    account = BankAccount.objects.all()
    if request.method == 'POST':
        # Handle direct bank transfer payment
        proof_of_payment = request.FILES.get('proof_of_payment')
        if proof_of_payment:
            order.proof_of_payment = proof_of_payment
            order.save()
            return redirect('direct_transfer_payment_confirmation', order_id=order.id)
    return render(request, 'order/direct_transfer_payment.html', {'order': order, 'account': account})

@login_required
def paystack_payment_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/payment_confirmation.html', {'order': order})

@login_required
def direct_transfer_payment_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order/payment_confirmation.html', {'order': order})
    

@csrf_exempt
@login_required
def paystack_callback(request):
    reference = request.GET.get('reference')
    url = f"https://api.paystack.co/transaction/verify/{reference}"
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
    }
    response = requests.get(url, headers=headers)
    response_data = response.json()
    
    if response_data['status']:
        transaction_data = response_data['data']
        try:
            # Retrieve the order using the pystk_ref field
            order = get_object_or_404(Order, pystk_ref=transaction_data['reference'])
            order.paid = True
            order.save()
            return redirect('order_detail', order_id=order.id)
        except Exception as e:
            print("Error updating order:", e)
    else:
        print("Transaction verification failed:", response_data)
    
    return JsonResponse(response_data)
    

@csrf_exempt
def paystack_webhook(request):
    payload = json.loads(request.body)
    event = payload.get('event')
    
    if event == 'charge.success':
        transaction_data = payload['data']
        reference = transaction_data['reference']
        try:
            # Retrieve the order using the pystk_ref field
            order = get_object_or_404(Order, pystk_ref=reference)
            order.paid = True
            order.save()
        except Exception as e:
            print("Error updating order:", e)
    
    return HttpResponse(status=200)