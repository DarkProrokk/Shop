from django.shortcuts import render
from django.views.generic import DetailView
from django.db import models
from .models import Cart


# Create your views here.


class CartView(DetailView):
    model = Cart
    template_name = 'Cart/cart.html'
    context_object_name = 'cart'

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(pk=1)
        return render(request, 'Cart/cart.html', {'cart': cart})
