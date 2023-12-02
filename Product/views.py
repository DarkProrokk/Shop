from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

from .models import Product


# Create your views here.
def index(request):
    return render(request, 'Product/index.html')


def test(request):
    prod = Product.objects.all()
    print(prod)
    return HttpResponse("<h1>Just Test Page</h1>")


class ProductListView(ListView):
    model = Product
    template_name = 'Product/all_products.html'
    context_object_name = 'products'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()  # Получение списка объектов модели
        allow_empty = self.get_allow_empty()
        context = self.get_context_data()
        return self.render_to_response(context)