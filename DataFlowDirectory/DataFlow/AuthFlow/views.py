from django.shortcuts import render
from django.views import View


def home(request):
    return render(request, 'AuthFlow/home.html')

# initial page if not logged in or new user
class SplashView(View):
    def get(self, request):
        return(render(request, 'AuthFlow/splash.html'))
    

# signup page
class SignupView(View):
    def get(self, request):
        return(render(request, 'AuthFlow/splash.html'))
    

# login page
class LoginView(View):
    def get(self, request):
        return(render(request, 'AuthFlow/splash.html'))
