from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import Order, Product, Restaurant
from .forms import OrderForm, RestaurantForm, AdminLoginForm
from django.contrib.auth.models import User  # type: ignore
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


# Create your views here.

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')  # Redireciona após salvar
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})


def order_success(request):
    return render(request, 'order_success.html')


def create_restaurant(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin_login')  # Apenas admins

    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                username=username, password=password)
            Restaurant.objects.create(
                name=form.cleaned_data['name'],
                location=form.cleaned_data['location'],
                login=user
            )
            return redirect('admin_dashboard')
    else:
        form = RestaurantForm()

    return render(request, 'create_restaurant.html', {'form': form})


def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    restaurant.delete()
    return redirect('admin_dashboard')


def restaurant_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Autenticar o usuário
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                # Verificar se o usuário está associado a um restaurante
                restaurant = Restaurant.objects.get(login=user)
                login(request, user)  # Inicia a sessão do usuário
                # Redireciona para o dashboard do gerente
                return redirect('dashboard')
            except Restaurant.DoesNotExist:
                messages.error(request, "Restaurant not found.")
        else:
            messages.error(request, "Invalid credentials.")
    form = AuthenticationForm()
    return render(request, 'restaurant_login.html', {'form': form})


def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_admin:  # Verifica se é um admin
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Invalid credentials or not an admin.")
    else:
        form = AdminLoginForm()

    restaurants = Restaurant.objects.all()
    orders = Order.objects.all()

    return render(request, 'admin_dashboard.html', {
        'restaurants': restaurants,
        'orders': orders
    })


def admin_dashboard(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin_login')  # Redireciona se não for admin

    restaurants = Restaurant.objects.all()
    orders = Order.objects.all()

    return render(request, 'admin_dashboard.html', {
        'restaurants': restaurants,
        'orders': orders
    })


def dashboard(request):
    try:
        # Recupera o restaurante associado ao usuário logado
        restaurant = Restaurant.objects.get(login=request.user)
    except Restaurant.DoesNotExist:
        # Se o restaurante não existir
        return render(request, 'error.html', {'message': "Restaurant not found."})

    # Recupera os produtos disponíveis ou outras informações específicas
    products = Product.objects.all()  # Podes filtrar se necessário
    # Encomendas relacionadas ao restaurante
    orders = Order.objects.filter(restaurant=restaurant)

    return render(request, 'dashboard.html', {
        'restaurant': restaurant,
        'products': products,
        'orders': orders
    })
