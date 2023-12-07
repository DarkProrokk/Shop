from django.contrib import admin

from .forms import CartItemForm
from .models import Cart, CartItem


class CartItemAdmin(admin.ModelAdmin):
    form = CartItemForm

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)

#TODO create custom admin for cart[COMPLETE]
