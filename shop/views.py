import stripe
from django.shortcuts import render, get_object_or_404
from cart.cart import Cart
from .models import Cake, Category
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse

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
    cakes = Cake.objects.all()  # Fetch all cakes from the database
    return render(request, 'shop/index.html', {'cakes': cakes})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    cakes = Cake.objects.filter(category=category)
    
    return render(request, 'shop/category_detail.html', {'category': category, 'cakes': cakes})

def cake_detail(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    
    return render(request, 'shop/cake_detail.html', {'cake': cake})

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})

def about(request):
    return render(request, 'shop/about.html')

def success(request):
    return render(request, 'shop/success.html')

def cancel(request):
    return render(request, 'shop/cancel.html')

def shop_home(request):
    categories = Category.objects.all()
    cakes = Cake.objects.all()
    return render(request, 'shop/home.html', {'categories': categories, 'cakes': cakes})

def home(request):
    return HttpResponse("<h1>Welcome to the Cake Shop!</h1><p>Go to <a href='/shop/'>Shop</a></p>")
