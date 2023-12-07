from django.urls import path

from .views import CartView

urlpatterns = [
    path('<int:pk>/', CartView.as_view(), name='cart'),
]