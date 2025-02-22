from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('cake/<int:cake_id>/', views.cake_detail, name='cake_detail'),
    path('create-checkout-session/', views.create_checkout_session, name='create _checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('about/', views.about, name='about'),
    ]