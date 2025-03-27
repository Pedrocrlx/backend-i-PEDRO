from django.urls import path
from . import views

urlpatterns = [
    path('create_order/', views.create_order.as_view(), name='create_order'),
]