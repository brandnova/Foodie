<<<<<<< HEAD
=======
import json
>>>>>>> master
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
=======
from django.db.models import Sum
from datetime import date, timedelta
from django.db.models.functions import TruncDate
>>>>>>> master
from order.models import Order
# from .decorators import prevent_authenticated_access
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserUpdateForm


# @prevent_authenticated_access
def login_view(request):
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

# @prevent_authenticated_access
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


<<<<<<< HEAD
@login_required
def dashboard_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'accounts/dashboard.html', {'orders': orders})

# accounts/views.py
=======
# @login_required
# def dashboard_view(request):
#     orders = Order.objects.filter(user=request.user)
#     return render(request, 'accounts/dashboard.html', {'orders': orders, })


@login_required
def dashboard_view(request):
    orders = Order.objects.filter(user=request.user, paid=True)
    orderss = Order.objects.filter(user=request.user,).order_by('-id')[:6]

    # Aggregate data by date
    daily_totals = (
        orders
        .annotate(date=TruncDate('created_at'))
        .values('date')
        .annotate(total_amount=Sum('items__price'))
        .order_by('date')[:5]
    )

    # Prepare data for the chart
    dates = [entry['date'].strftime('%Y-%m-%d') for entry in daily_totals]
    amounts = [float(entry['total_amount']) for entry in daily_totals]

    context = {
        'dates': json.dumps(dates),
        'amounts': json.dumps(amounts),
        'orderss': orderss,
    }

    return render(request, 'accounts/dashboard.html', context)

@login_required
def user_order(request):
    orderss = Order.objects.filter(user=request.user).order_by('created_at')
    return render(request, 'accounts/user_order.html', {'orderss': orderss})


>>>>>>> master

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
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
        'user_form': user_form
        })
