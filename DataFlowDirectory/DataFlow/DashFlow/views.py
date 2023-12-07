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



def dash_view(request):

    api_url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

    ## prints response code of api call
    # response = requests.get(api_url)
    # print(f"The response status code is: {response.status_code}")

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            print(data['bitcoin'])
            # print(data['usd'])
    except Exception as e:
        print(e)

    context = {'data': data['bitcoin']}

    return render(request, 'DashFlow/dashboard.html', context)


# class DashView(View):

#     template_name = 'DashFlow/dashboard.html'

#     def get(self, request, *args, **kwargs):

#         # CoinGecko api for current price of btc
#         # api_url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

#         api_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BTCUSD&from=2011-01-01&to=2023-11-30&apikey={alpha_vantage_api_key}"

#         # example of alpha vantage api response
#         """'Time Series (Daily)': {
#         "2023-11-30": {
#             "1. open": "37860.2961",
#             "2. high": "38165.9514",
#             "3. low": "37589.7859",
#             "4. close": "37808.2546",
#             "5. volume": "4110"
#         },"""

#         data = {}

#         try:
#             response = requests.get(api_url)
#             if response.status_code == 200:
#                 data = response.json()

#                  # test in the terminal
#                 print(data['Time Series (Daily)']['2023-11-30']['4. close']) # returns string of closing price

#         except Exception as e:
#             print(e)

#         # dict.get() is a type of error handling as it returns the second arg as default if key not found
#         data = data.get(str(round(float(data['Time Series (Daily)']['2023-11-30']['4. close']), 2)))

#         context = {'data': data} 

#         return render(request, self.template_name, context)


class DashView(View):

    template_name = 'DashFlow/dashboard.html'

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

        # print the type of each value in the queryset
        print((data_for_chart))
    
        context = {'data': btcData,
                   'btc_chart_data': btc_chart_data,
                   'eth_chart_data': eth_chart_data,
                   'data_for_chart_json': data_for_chart_json,
                   } 

        return render(request, self.template_name, context)