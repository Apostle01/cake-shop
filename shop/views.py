from django.shortcuts import render
from .models import Cake, Category

def index(request):
    categories = Category.objects.all()
    cakes = Cake.objects.all()
    
    return render(request, 'shop/index.html', {'categories': categories, 'cakes': cakes})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    cakes = Cake.objects.filter(category=category)
    
    return render(request, 'shop/category_detail.html', {'category': category, 'cakes': cakes})

def cake_detail(request, cake_id):
    cake = Cake.objects.get(id=cake_id)
    
    return render(request, 'shop/cake_detail.html', {'cake': cake})
