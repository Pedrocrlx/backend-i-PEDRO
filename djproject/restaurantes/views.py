from django.shortcuts import redirect, render

# Create your views here.
from .models import Order
from .forms import OrderForm

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')  # Redireciona após salvar
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})
