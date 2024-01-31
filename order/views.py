from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from cart.models import UserCart
from .forms import OrderUserDataForm
from .models import Order, OrderItem

@login_required
def sumbit(request):
    if request.method == 'POST':
        form = OrderUserDataForm(request.POST)

        if form.is_valid():
            order = Order()
            order.user = request.user

            order.save()

            orderUserData = form.save(commit=False)
            orderUserData.order = order

            items = UserCart.objects.filter(user=request.user)

            for item in items:
                itemModel = OrderItem()
                itemModel.price = item.item.price
                itemModel.quantity = item.quantity
                itemModel.item = item.item
                itemModel.order = order

                itemModel.save()

            orderUserData.save()

            delete_from_cart = UserCart.objects.filter(user=request.user)

            delete_from_cart.delete()

            messages.info(request, 'Zamówienie zostało złożone')

            return redirect('/cart/cart')
    else:
        items = UserCart.objects.all()
        total_sum = UserCart.total_sum(items)
        form = OrderUserDataForm()

    return render(request, 'order/submit.html', {
        'items': items,
        'total_sum': total_sum,
        'form': form
    })

@login_required
def history(request):
    orders = Order.objects.filter(user=request.user)

    return render(request, 'order/history.html', {
        'orders': orders
    })

def details(request, pk):
    order = get_object_or_404(Order, pk=pk)

    items = order.order_item.all()
    orderData = order.order_data.first()

    total_price = UserCart.total_sum(items)

    return render(request, 'order/details.html', {
        'order': order,
        'items': items,
        'orderData': orderData,
        'total_price': total_price
    })
