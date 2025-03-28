from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_login, name='login'),  # Página principal
    path('dashboard/', views.dashboard, name='dashboard'),  # Página do dashboard (a criar)
    path('create_order/', views.create_order, name='create_order'),
    path('order_success/', views.order_success, name='order_success'),  # Página de sucesso
    path('create_restaurant/', views.create_restaurant, name='create_restaurant'),
    path('list_orders/', views.order_success, name='admin_dashboard'),
]