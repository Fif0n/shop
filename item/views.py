from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Item, Category

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'item/detail.html', {
        'item': item,
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