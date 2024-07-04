from django.contrib import admin
from .models import Category, MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')  # Include image field

admin.site.register(Category)
