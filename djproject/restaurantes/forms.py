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
