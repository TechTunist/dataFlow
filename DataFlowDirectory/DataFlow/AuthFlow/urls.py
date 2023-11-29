from django.urls import path, include
from .views import SplashView, SignupView, LoginView

urlpatterns = [
    path('', SplashView.as_view(), name='splash'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]