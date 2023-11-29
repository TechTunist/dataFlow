from django.urls import path, include
from .views import DashView

urlpatterns = [
    path('', DashView.as_view(), name='dashboard'),
    # path('', dash_view),
]