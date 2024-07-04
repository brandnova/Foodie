from django.db import models
from django.conf import settings
from cart.models import CartItem
    
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
<<<<<<< HEAD
=======
    phone = models.CharField(max_length=15, null=True)
>>>>>>> master
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    extra_details = models.TextField(blank=True)
    paid = models.BooleanField(default=False)
    proof_of_payment = models.ImageField(upload_to='proofs_of_payment/', blank=True, null=True)
    payment_reference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} - {self.email}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey('menu.MenuItem', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.menu_item.name}'

    def get_cost(self):
        return self.price * self.quantity

class BankAccount(models.Model):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    account_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"