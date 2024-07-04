from django.urls import path
from .views import (
    order_create, order_detail, payments_select, paystack_payment, paystack_callback, 
    paystack_webhook, direct_transfer_payment, paystack_payment_confirmation, 
    direct_transfer_payment_confirmation
)

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('<int:order_id>/', order_detail, name='order_detail'),
    path('payments/<int:order_id>/', payments_select, name='payments'),
    path('paystack/<int:order_id>/', paystack_payment, name='paystack_payment'),
    path('paystack/callback/', paystack_callback, name='paystack_callback'),
    path('paystack/webhook/', paystack_webhook, name='paystack_webhook'),
    path('direct_transfer/payment/<int:order_id>/', direct_transfer_payment, name='direct_transfer_payment'),
    path('direct_transfer/payment/<int:order_id>/confirmation/', direct_transfer_payment_confirmation, name='direct_transfer_payment_confirmation'),
]
