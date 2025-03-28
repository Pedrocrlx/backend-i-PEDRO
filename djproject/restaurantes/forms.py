from django import forms
from .models import Order, ProductOrder

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['restaurant', 'products']  # Altere conforme necessário

class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = ['product', 'quantity']  # Campos relevantes

class RestaurantLoginForm(forms.Form):
    restaurant_name = forms.CharField(label="Restaurant Name", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
