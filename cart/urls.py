from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),  # Cart detail page
    path('add/<int:cake_id>/', views.add_to_cart, name='add_to_cart'),  # Add to cart
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),  # Remove from cart
]
