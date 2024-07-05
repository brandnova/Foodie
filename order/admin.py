from django.contrib import admin
from .models import Order, OrderItem, BankAccount
from .views import send_order_status_update_email  # Import your email function

# Register the OrderItem model as an inline within the Order admin page
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['menu_item']

# Register the Order model with custom display options
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'postal_code', 'city', 'paid', 'created_at', 'updated_at']
    list_filter = ['paid', 'created_at', 'updated_at']
    inlines = [OrderItemInline]

    def save_model(self, request, obj, form, change):
        if change:  # Only send email on updates
            old_order = Order.objects.get(id=obj.id)
            if old_order.paid != obj.paid:  # Check if the paid status has changed
                send_order_status_update_email(obj)  # Send email if status changed
        super().save_model(request, obj, form, change)

# Register the OrderItem model separately if needed
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'menu_item', 'price', 'quantity']
    list_filter = ['order__created_at', 'menu_item__category']
    search_fields = ['menu_item__name']

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ['bank_name', 'account_number', 'account_name']
