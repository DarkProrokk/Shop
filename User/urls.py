from django.urls import path
from .views import LoginView, RegisterView, UserView, logoutView
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', RegisterView.as_view()),
    path('', UserView.as_view(), name='user'),
    path('logout/', logoutView),
]