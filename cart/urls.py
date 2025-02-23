from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_home, name='cart_home'),  # Example view
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:cake_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
