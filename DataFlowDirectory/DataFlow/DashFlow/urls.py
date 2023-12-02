from django.urls import path, include
from .views import DashView
from . import api

urlpatterns = [
    path('', DashView.as_view(), name='dashboard'),
    path('api/price', api.price, name='price'),
    path('api/price_by_date', api.price_by_date, name='price_by_date'),
]