from django.urls import path
from .views import menu_list_view, menu_item_detail_view

urlpatterns = [
    path('', menu_list_view, name='menu_list'),
    path('item/<int:pk>/', menu_item_detail_view, name='menu_item_detail'),
]
