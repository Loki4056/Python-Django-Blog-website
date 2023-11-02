from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.contrib.auth.views import LoginView
from django.urls import reverse

class LoginView(LoginView):
    template_name = 'users/login.html'

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            # Redirect to the 'login' view using the URL name
            return redirect(reverse('login'))
        else:
            return render(request, 'users/register.html', {'form': form})