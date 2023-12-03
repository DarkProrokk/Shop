from django.urls import path

from .views import AddItemInCart

urlpatterns = [
    path('add_item/<int:pk>/', AddItemInCart.as_view(), name='add_item'),
]