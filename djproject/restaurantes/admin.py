from django.contrib import admin

# Register your models here.

from .models import Restaurant, Product, Order, ProductOrder

admin.site.register(Restaurant)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductOrder)
