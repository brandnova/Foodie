from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from cart.models import Cart
from .models import MenuItem, Category

def menu_list_view(request):
    query = request.GET.get('q')
    categories = Category.objects.all()
    if query:
        categories = categories.filter(
            Q(items__name__icontains=query) | 
            Q(name__icontains=query) | 
            Q(items__description__icontains=query) |
            Q(items__price__icontains=query)
        ).distinct()
    cart = get_object_or_404(Cart, user=request.user)
    cart_count = cart.items.count()
    return render(request, 'menu/menu_list.html', {'categories': categories, 'cart_count': cart_count, 'query': query})

def menu_item_detail_view(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    cart = get_object_or_404(Cart, user=request.user)
    cart_count = cart.items.count()
    return render(request, 'menu/menu_item_detail.html', {'item': item, 'cart_count': cart_count,})
