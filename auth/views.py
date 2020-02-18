from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView as Logout
from django.http import HttpResponse

class Login(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = False
   