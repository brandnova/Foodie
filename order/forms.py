from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
<<<<<<< HEAD
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'extra_details']
=======
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'postal_code', 'city', 'extra_details']
>>>>>>> master
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
<<<<<<< HEAD
=======
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
>>>>>>> master
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'extra_details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Details', 'rows': 3}),
        }

class PaystackPaymentForm(forms.Form):
    email = forms.EmailField(label='Email')
    amount = forms.DecimalField(label='Amount', min_value=0.01)