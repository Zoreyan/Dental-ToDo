from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from .filters import OrderFilter

def order_list(request):
    orders = Order.objects.all().order_by('-id')
    order_filter = OrderFilter(request.GET, queryset=orders)
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    if request.method == 'POST' and 'delete' in request.POST:
        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        order.delete()
        return redirect('order_list')
    context = {
        'orders': orders,
        'form': form,
        'filter': order_filter
    }
    return render(request, 'app/index.html', context)
