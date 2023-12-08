from django.shortcuts import render
from django.views import View
import requests
from .models import BitcoinDaily, EthereumDaily
import os
from dotenv import load_dotenv

from rest_framework import generics
from .serializers import BitcoinDailySerializer
import json


load_dotenv()

alpha_vantage_api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

class DashView(View):

    template_name = 'DashFlow/dashboard-tradingview.html'

    def get(self, request, *args, **kwargs):

        data = {}

        try:
            btcData = BitcoinDaily.objects.all().order_by('date')
            btc_chart_data = {
                "date": [d.date.strftime("%Y-%m-%d") for d in btcData],
                "close": [round(float(d.close), 2) for d in btcData]
            }

        except Exception as e:
            print(e)

        # eth data
        try:
            ethData = EthereumDaily.objects.all().order_by('date')
            eth_chart_data = {
                "date": [d.date.strftime("%Y-%m-%d") for d in ethData],
                "close": [round(float(d.close), 2) for d in ethData]
            }

        except Exception as e:
            print(e)

        # create object formatted for lightweight charts
        bitcoin_data = BitcoinDaily.objects.order_by('date')

        data_for_chart = []
        for entry in bitcoin_data:
            formatted_entry = {
                'time': entry.date.strftime('%Y-%m-%d'),
                'value': int(entry.close)  # Assuming you are using 'close' field
            }
            data_for_chart.append(formatted_entry)
            data_for_chart_json = json.dumps(data_for_chart)
    
        context = {'data': btcData,
                   'btc_chart_data': btc_chart_data,
                   'eth_chart_data': eth_chart_data,
                   'data_for_chart_json': data_for_chart_json,
                   } 

        return render(request, self.template_name, context)