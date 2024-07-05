from django.urls import path
from .views import login_view, logout_view, register_view, dashboard_view, profile
from .views import login_view, logout_view, register_view, dashboard_view, profile, user_order

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('orders/', user_order, name='orders'), 
]
