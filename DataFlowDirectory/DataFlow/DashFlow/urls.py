from django.urls import path, include
from .views import DashView
from . import api

urlpatterns = [
    path('', DashView.as_view(), name='dashboard'),
    path('api/btc/data', api.btc_all_data, name='price'),
    path('api/btc/price/<str:start_date>', api.btc_price_by_date, name='btc_price_by_date'),
    path('api/btc/price/', api.btc_price_all, name='btc_price_all'),
    path('api/person/', api.person, name='person'),
]