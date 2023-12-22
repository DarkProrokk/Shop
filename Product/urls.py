from django.urls import path
from .views import index, test, ProductListView


urlpatterns = [
    path('', index),
    path('test/', test),
    path('items/', ProductListView.as_view(), name='catalog'),
]