from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('cake/<int:cake_id>/', views.cake_detail, name='cake_detail'),  # Cake detail page
]
