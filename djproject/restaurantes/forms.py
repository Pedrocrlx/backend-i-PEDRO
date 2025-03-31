from django import forms
from .models import ProductOrder, Product

class CreateOrderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicionar campos dinamicamente para cada produto
        for product in Product.objects.all():
            self.fields[str(product.id)] = forms.IntegerField(
                label=product.name,
                min_value=0,  # Quantidade mínima
                initial=0,    # Começa com 0 como padrão
                required=False
            )

class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = ['product', 'quantity', 'order']  # Campos relevantes
         
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

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category']