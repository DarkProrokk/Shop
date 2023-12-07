from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from rest_framework import viewsets

from Cart.forms import CartItemForm
from Cart.models import CartItem
from .models import Product, Mark
from .serializers import ProductSerializer, MarkSerializer


# Create your views here.
def index(request):
    return render(request, 'Product/index.html')


def test(request):
    return HttpResponse("<h1>Just Test Page</h1>")


class ProductListView(ListView):
    form_class = CartItemForm
    model = Product
    template_name = 'Product/all_products.html'
    context_object_name = 'products'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        context['form'] = self.form_class()

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()

        context = self.get_context_data()
        form = self.form_class(request.POST)
        context['form'] = form
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart = form.cleaned_data['cart']
            product = form.cleaned_data['product']
            CartItem.objects.create(quantity=quantity, cart=cart, product=product)
        else:
            # Если форма не прошла валидацию, добавьте ошибки формы в контекст шаблона
            context['form_errors'] = form.errors
        return self.render_to_response(context)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
