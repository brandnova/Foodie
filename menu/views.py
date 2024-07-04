from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Category

def menu_list_view(request):
    categories = Category.objects.all()
    return render(request, 'menu/menu_list.html', {'categories': categories})

def menu_item_detail_view(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    return render(request, 'menu/menu_item_detail.html', {'item': item})
