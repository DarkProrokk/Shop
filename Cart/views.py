from django.shortcuts import HttpResponse
from django.views import View


# Create your views here.


class AddItemInCart(View):

    def post(self, request, pk):
        print(request, pk)
        return HttpResponse("Предмет добавлен")
