"""
URL configuration for cakeshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from shop.views import home  # Import the home view
from cart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Allauth URLs
    path('shop/', include('shop.urls', namespace='shop')),  # Include shop app URLs
    path('another-shop/', include('shop.urls', namespace='another_shop')),  # Unique namespace
    path('cart/', include('cart.urls', namespace='cart')),  # Include cart app URLs
    path('', home, name='home'),  # Add this line for the homepage
    path('', include('shop.urls')),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
