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
        
class AdminLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class RestaurantLoginForm(forms.Form):
    restaurant_name = forms.CharField(label="Restaurant Name", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class RestaurantForm(forms.Form):
    name = forms.CharField(label="Restaurant Name", max_length=100)
    location = forms.CharField(label="Location", max_length=100)
    username = forms.CharField(label="Manager Username", max_length=100)
    password = forms.CharField(label="Manager Password", widget=forms.PasswordInput)
