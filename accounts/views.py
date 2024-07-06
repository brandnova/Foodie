import json
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.core.paginator import Paginator
from datetime import date, timedelta
from django.db.models.functions import TruncDate
from cart.models import Cart
from order.models import Order
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserUpdateForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard_view(request):
    # Fetch orders and recent orders
    orders = Order.objects.filter(user=request.user, paid=True)
    orderss = Order.objects.filter(user=request.user).order_by('-id')[:6]
    
    # Try to get the user's cart or create a new one if it doesn't exist
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)

    cart_count = cart.items.count()

    # Aggregate data by date for chart
    daily_totals = (
        orders
        .annotate(date=TruncDate('created_at'))
        .values('date')
        .annotate(total_amount=Sum('items__price'))
        .order_by('date')[:6]
    )

    # Prepare data for the chart
    dates = [entry['date'].strftime('%Y-%m-%d') for entry in daily_totals]
    amounts = [float(entry['total_amount']) for entry in daily_totals]

    context = {
        'dates': json.dumps(dates),
        'amounts': json.dumps(amounts),
        'orderss': orderss,
        'cart_count': cart_count,
    }

    return render(request, 'accounts/dashboard.html', context)

@login_required
def user_order(request):
    orderss = Order.objects.filter(user=request.user).order_by('created_at')
    cart = get_object_or_404(Cart, user=request.user)
    cart_count = cart.items.count()

    paginator = Paginator(orderss, 5)  # Show 5 orders per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'accounts/user_order.html', {'orderss': orderss, 'page_obj': page_obj, 'cart_count': cart_count,})



@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    cart = get_object_or_404(Cart, user=request.user)
    cart_count = cart.items.count()

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            # messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    
    return render(request, 'accounts/profile.html', {
        'orders': orders, 
        'user_form': user_form,
        'cart_count': cart_count,
        })
