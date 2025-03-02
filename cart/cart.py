from decimal import Decimal
from django.conf import settings
from shop.models import Cake  # Replace with your product model

class Cart:
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, cake, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        cake_id = str(cake.id)
        if cake_id not in self.cart:
            self.cart[cake_id] = {
                'quantity': 0,
                'price': str(cake.price),
            }
        if override_quantity:
            self.cart[cake_id]['quantity'] = quantity
        else:
            self.cart[cake_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        Mark the session as modified to ensure it gets saved.
        """
        self.session.modified = True

    def remove(self, cake):
        """
        Remove a product from the cart.
        """
        cake_id = str(cake.id)
        if cake_id in self.cart:
            del self.cart[cake_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        """
        cake_ids = self.cart.keys()
        # Get the product objects and add them to the cart
        cakes = Cake.objects.filter(id__in=cake_ids)
        cart = self.cart.copy()
        for cake in cakes:
            cart[str(cake.id)]['cake'] = cake
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Calculate the total cost of the items in the cart.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Remove the cart from the session.
        """
        del self.session[settings.CART_SESSION_ID]
        self.save()