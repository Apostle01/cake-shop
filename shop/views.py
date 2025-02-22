import stripe
from django.shortcuts import render
from .models import Cake, Category
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session_session(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency':
'usd',
'product_data': {
    'Cake Order',
                           },
                           'unit_amount':
2000, # $20.00
                        },
                        'quantity': 1,
                        },
                        ],
                        mode='payment',
success_url=request.build_absolute_uri('/shop/success/'),
cancel_url=request.build_absolute_uri('/shop/cancel/'),
    )
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)})

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

def about(request):
    return render(request, 'shop/about.html')

def success(request):
    return render(request, 'shop/success.html')
