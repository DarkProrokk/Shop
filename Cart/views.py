from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.db import models
from .models import Cart
from django.db.models import F

# Create your views here.


class CartView(DetailView):
    model = Cart
    template_name = 'Cart/cart.html'
    context_object_name = 'cart'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        cart = Cart.objects.get(pk=request.user.id)
        cart_items = cart.products.all().annotate(total_price=(F('product__payment__price') * F('quantity')))
        return render(request, 'Cart/cart.html', {'cart': cart_items})
