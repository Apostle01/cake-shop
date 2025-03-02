# cart/urls.py
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:cake_id>/', views.cart_add, name='cart_add'),  # Use 'cart_add' instead of 'add_to_cart'
    path('remove/<int:cake_id>/', views.cart_remove, name='cart_remove'),
]