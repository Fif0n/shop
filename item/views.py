from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Item, Category, Opinion
from .forms import OpinionForm

from order.models import OrderItem

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    bought = OrderItem.objects.filter(item=item, order__user=request.user)
    opinions = item.opinion.all()

    ratings_avg = Opinion.opinion_avg(opinions)

    return render(request, 'item/detail.html', {
        'item': item,
        'bought': bought,
        'opinions': opinions,
        'ratings_avg': ratings_avg
    })

def items(request):
    queryName = request.GET.get('name', '')
    queryCategory = request.GET.getlist('category', '')

    categories = Category.objects.all()

    items = Item.objects.all()

    if queryName:
        items = items.filter(Q(name__icontains=queryName))

    if queryCategory:
        items = items.filter(category__id__in=queryCategory)
    
    queryCategory = [ int(i) for i in queryCategory ]

    return render(request, 'item/items.html', {
        'items': items,
        'categories': categories,
        'queryName': queryName,
        'queryCategory': queryCategory
    })

@login_required
def opinion(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = OpinionForm(request.POST)

        if form.is_valid():
            opinion = form.save(commit=False)

            opinion.created_by = request.user
            opinion.item = item

            opinion.save()

            messages.info(request, 'Dodano opinię. Dziękujemy!')

            return redirect(f'/item/detail/{pk}')
    else:
        form = OpinionForm()

    return render(request, 'item/opinion.html', {
        'form': form,
        'item': item
    })