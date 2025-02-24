from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about/', views.about, name='about'),  # Add this line for the about page
    path('cake/<int:cake_id>/', views.cake_detail, name='cake_detail'),  # Cake detail page
]
