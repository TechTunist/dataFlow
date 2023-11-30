from django.shortcuts import render
from django.views import View
import requests

import os
from dotenv import load_dotenv

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
    except:
        pass

    context = {'data': data['bitcoin']}

    return render(request, 'DashFlow/dashboard.html', context)


class DashView(View):

    template_name = 'DashFlow/dashboard.html'

    def get(self, request, *args, **kwargs):

        # CoinGecko api for current price of btc
        # api_url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

        api_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BTCUSD&from=2011-01-01&to=2023-11-30&apikey={alpha_vantage_api_key}"

        """'Time Series (Daily)': {
        "2023-11-30": {
            "1. open": "37860.2961",
            "2. high": "38165.9514",
            "3. low": "37589.7859",
            "4. close": "37808.2546",
            "5. volume": "4110"
        },"""

        data = {}

        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                print(data['Time Series (Daily)']['2023-11-30']['4. close']) # test in the terminal
        except Exception as e:
            print(e)

        # dict.get() is a type of error handling as it returns the second arg as default if key not found
        context = {'data': data.get('bitcoin', "ERROR: data not found!")} 

        return render(request, self.template_name, context)
