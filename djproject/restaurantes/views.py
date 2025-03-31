from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Order, Product, ProductOrder, Restaurant
from .forms import CreateOrderForm, ProductForm, RestaurantForm, AdminLoginForm
from django.contrib.auth.models import User  # type: ignore
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here. 

def create_order(request):
    if not request.user.is_authenticated:
        return redirect('restaurant_login')  # Garantir que o usuário está logado

    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            # Criar a encomenda associada ao restaurante do usuário
            restaurant = request.user.restaurant  # Presume que existe um `Restaurant` associado ao `User`
            order = Order.objects.create(restaurant=restaurant)

            # Processar os produtos selecionados e quantidades
            for product_id, quantity in form.cleaned_data.items():
                if quantity > 0:
                    product = Product.objects.get(id=product_id)
                    ProductOrder.objects.create(order=order, product=product, quantity=quantity)

            return redirect('order_success')  # Redireciona após salvar
    else:
        form = CreateOrderForm()

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
            if user is not None and user.is_staff:  # Verifica se é um admin
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Invalid credentials or not an admin.")
    else:
        form = AdminLoginForm()

    return render(request, 'admin_login.html', {
        'form': form,
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


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Redireciona para uma lista de produtos
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('restaurant_login')  # Redirect to the login page after logout