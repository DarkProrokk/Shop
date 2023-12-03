from django.urls import path
from .views import LoginView, RegisterView, UserView
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', RegisterView.as_view()),
    path('<slug:slug>/', UserView.as_view(), name='user')
]