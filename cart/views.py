from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, OrderItem
from shop.models import Cake

# Helper function to get or create a cart for the user
def get_cart(request):
    if request.user.is_authenticated:
        # For authenticated users, use their user ID
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # For anonymous users, use the session key
        if not request.session.session_key:
            request.session.create()
        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart

@login_required
def cart_detail(request):
    cart = get_cart(request)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.total_price for item in cart_items)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    cart = get_cart(request)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, cake=cake)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart_detail')

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart:cart_detail')

def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart:cart_detail')