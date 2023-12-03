from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.views.generic import DetailView
# Create your views here.
from .forms import LoginForm, RegistrationForm
from .models import CustomUser


class LoginView(View):
    form_class = LoginForm
    template_name = "User/login.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user')
            else:
                return HttpResponse("<h1> Invalid login or password </h1>")
        return render(request, self.template_name, {'form': form})


class RegisterView(View):
    form_class = RegistrationForm
    template_name = "User/register.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            CustomUser.objects.create_user(username=username, password=password)
        return render(request, self.template_name, {'form': form})


class UserView(DetailView):
    model = CustomUser
    template_name = "User/user.html"
    context_object_name = 'user'

    # def get(self, request, username):
    #     user = self.get_object()
    #     return render(request, self.template_name, {'user': user})