from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from shop.models import Cake
from .models import Cart, CartItem

def cart_home(request):
    return HttpResponse("This is the Cart page.")

def cart_detail(request):
    cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def add_to_cart(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, cake=cake)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart_detail')

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart:cart_detail')



