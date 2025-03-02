# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Cake  # Replace with your product model
from .cart import Cart  # Import the Cart class
from .forms import CartAddProductForm, CakeForm   # Import the form

def cart_detail(request):
    """
    Display the contents of the cart.
    """
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True}
        )
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def cart_add(request, cake_id):
    """
    Add a product to the cart or update its quantity.
    """
    cart = Cart(request)
    cake = get_object_or_404(Cake, id=cake_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(cake, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')

def cart_remove(request, cake_id):
    """
    Remove a product from the cart.
    """
    cart = Cart(request)
    cake = get_object_or_404(Cake, id=cake_id)
    cart.remove(cake)
    return redirect('cart:cart_detail')

def add_cake(request):
    if request.method == 'POST':
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:index')
    else:
        form = CakeForm()
    return render(request, 'shop/add_cake.html', {'form': form})