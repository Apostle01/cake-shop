import stripe
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from cart.cart import Cart
from .models import Cake, Category, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import CakeForm

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Cake Order',
                        },
                        'unit_amount': 2000,  # $20.00
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
    category = get_object_or_404(Category, id=category_id)
    cakes = Cake.objects.filter(category=category)
    return render(request, 'shop/category_detail.html', {'category': category, 'cakes': cakes})

def cake_detail(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    related_cakes = Cake.objects.filter(category=cake.category).exclude(id=cake.id)[:3]  # Example logic
    form = CakeForm()  # Form for adding a new cake
    return render(request, 'shop/cake_detail.html', {
        'cake': cake,
        'related_cakes': related_cakes,
        'form': form,
    })

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})

def about(request):
    return render(request, 'shop/about.html')

def success(request):
    return render(request, 'shop/success.html')

def cancel(request):
    return render(request, 'shop/cancel.html')

def home(request):
    cakes = Cake.objects.all()  # Query all products
    return render(request, 'shop/home.html', {'cakes': cakes})

@login_required
def profile(request):
    return render(request, 'account/profile.html')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'shop/order_detail.html', {'order': order})

def search(request):
    query = request.GET.get('q')
    if query:
        cakes = Cake.objects.filter(Q(name__icontains=query) | Q(category__name__icontains=query))
    else:
        cakes = Cake.objects.all()
    return render(request, 'shop/index.html', {'cakes': cakes})

def orderitem_detail(request, orderitem_id):
    orderitem = get_object_or_404(OrderItem, id=orderitem_id)
    return render(request, 'shop/orderitem_detail.html', {'orderitem': orderitem})

@login_required
def checkout(request):
    # Add your checkout logic here
    return render(request, 'shop/checkout.html')