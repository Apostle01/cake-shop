from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about/', views.about, name='about'),  # Add this line for the about page
    path('cake/<int:cake_id>/', views.cake_detail, name='cake_detail'),  # Cake detail page
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orderitem/', views.orderitem, name='orderitem'),
    path('orderitem/<int:orderitem_id>/', views.orderitem_detail, name='orderitem_detail'),
    path('search/', views.search, name='search'),
]
