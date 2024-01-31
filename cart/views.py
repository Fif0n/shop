from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserCart
from item.models import Item


@login_required
def cart(request):
    cart_items = UserCart.objects.filter(user=request.user)

    totla_sum = UserCart.total_sum(cart_items)

    return render(request, 'cart/cart.html', {
        'items': cart_items,
        'totla_sum': totla_sum
    })

@login_required
def add(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.quantity <= 0:
        messages.info(request, 'Brak danego przedmiotu na magazynie')

        return redirect(f'/item/detail/{item_pk}')

    if UserCart.objects.filter(item=item, user=request.user).exists():
        messages.info(request, 'Dany przedmiot już jest w twoim koszyku')

        return redirect(f'/item/detail/{item_pk}')

    cart = UserCart()

    cart.item = item
    cart.user = request.user
    cart.quantity = request.POST.get('quantity')

    cart.save()
    messages.info(request, 'Dodano przedmiot do koszyka')

    return redirect(f'/item/detail/{item_pk}')

@login_required
def remove(request, pk):
    cart_item = get_object_or_404(UserCart, pk=pk)

    cart_item.delete()

    messages.info(request, 'Usunięto przedmiot z koszyka')

    return redirect('/cart/cart/')


@login_required
def change_quantity(request, pk):
    cart_item = get_object_or_404(UserCart, pk=pk)

    action_type = request.POST.get('action')
    
    if action_type == 'add':
        cart_item.quantity += 1

        if cart_item.item.quantity < cart_item.quantity:
            messages.info(request, 'Ilość przekraca ilość sztuk na magazynie')

            return redirect('/cart/cart/')
    
    if action_type == 'subtract':
        cart_item.quantity -= 1

        if cart_item.quantity <= 0:
            messages.info(request, 'Ilość nie może być mniejsza niż 1')

            return redirect('/cart/cart/')

    cart_item.save()

    messages.info(request, 'Zmieniono ilość')

    return redirect('/cart/cart/')


    


    