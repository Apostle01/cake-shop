from django.db import models
from django.utils.translation import gettext_lazy as _
from shop.models import Cake  # Import the Cake model from the shop app

class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = ('-created_at',)

    def __str__(self):
        return f"Cart {self.id} (Created: {self.created_at})"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name=_('cart'), related_name='items')
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE, verbose_name=_('cake'))
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'), default=1)

    class Meta:
        verbose_name = _('cart item')
        verbose_name_plural = _('cart items')
        ordering = ('cart',)

    def __str__(self):
        return f"{self.quantity} x {self.cake.name}"

    @property
    def total_price(self):
        return self.cake.price * self.quantity