from pyexpat.errors import messages
from django.shortcuts import redirect, render

# Create your views here.
from .models import Order, Product, Restaurant
from .forms import OrderForm, RestaurantLoginForm

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
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_restaurant')  # Redireciona após salvar
    else:
        form = OrderForm()
    return render(request, 'create_restaurant.html', {'form': form})

def restaurant_login(request):
    if request.method == 'POST':
        form = RestaurantLoginForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['restaurant_name']
            password = form.cleaned_data['password']

            # Verifica se o restaurante existe
            try:
                restaurant = Restaurant.objects.get(name=restaurant_name)
            except Restaurant.DoesNotExist:
                messages.error(request, "Restaurant not found.")
                return redirect('login')

            # Autenticar o login do restaurante
            user = authenticate(request, username=restaurant.login.username, password=password) # type: ignore
            if user is not None:
                login(request, user) # type: ignore
                return redirect('dashboard')  # Redirecionar para o dashboard após login
            else:
                messages.error(request, "Invalid credentials.")
    else:
        form = RestaurantLoginForm()

    return render(request, 'restaurant_login.html', {'form': form})

def dashboard(request):
    # Verifica se o usuário está autenticado e associado a um restaurante
    try:
        restaurant = Restaurant.objects.get(login=request.user)
    except Restaurant.DoesNotExist:
        restaurant = None

    # Recupera os produtos disponíveis para encomenda
    products = Product.objects.all()

    return render(request, 'dashboard.html', {'restaurant': restaurant, 'products': products})