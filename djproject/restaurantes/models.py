from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    login = models.OneToOneField(User, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='ProductOrder')
    created_at = models.DateTimeField(auto_now_add=True)

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
