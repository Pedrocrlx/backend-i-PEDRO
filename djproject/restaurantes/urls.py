from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_login, name='restaurant_login'),  # Página principal
    path('dashboard/', views.dashboard, name='dashboard'),  # Página do dashboard
    path('mezzero/login/', views.admin_login, name='admin_login'),
    path('mezzero/create_product/', views.create_product, name='create_product'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_success/', views.order_success, name='order_success'),  # Página de sucesso
    path('mezzero/create_restaurant/', views.create_restaurant, name='create_restaurant'),
    path('mezzero/admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.logout_view, name='logout'),
]