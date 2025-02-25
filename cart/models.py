from django.db import models
from django.contrib.auth.models import User
from shop.models import Cake

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    checked_out = models.BooleanField(default=False)  # ✅ Keep only one Cart model

    def __str__(self):
        if self.user:
            return f"Cart for {self.user.username}"
        return f"Cart for session {self.session_key}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.cake.name}"

    @property
    def total_price(self):
        return self.cake.price * self.quantity

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cake(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
