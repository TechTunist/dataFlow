#
#
#
#
# currently imports entire history of ETH
#
#
#
#




from django.core.management.base import BaseCommand
import requests
from DashFlow.models import BitcoinDailyMeta, BitcoinDaily, EthereumDailyMeta, EthereumDaily
import datetime

# load the alpha vantage api key for btc time series data in .env
import os
from dotenv import load_dotenv
load_dotenv()
alpha_vantage_api_key = os.getenv('ALPHA_VANTAGE_API_KEY')


class Command(BaseCommand):
    help = "Fetches and stores Bitcoin daily data"

    def handle(self, *args, **kwargs):
        api_endpoint = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=ETHUSD&apikey={alpha_vantage_api_key}"        
        
        params = {'api_key': alpha_vantage_api_key}

        response = requests.get(api_endpoint, params=params)
        data = response.json()

        # parse and save the Meta Data
        meta_data = data['Meta Data']
        meta = EthereumDailyMeta.objects.create(
            information=meta_data['1. Information'],
            symbol=meta_data['2. Symbol'],
            last_refreshed=datetime.datetime.strptime(meta_data['3. Last Refreshed'], '%Y-%m-%d').date(),
            output_size=meta_data['4. Output Size'],
            time_zone=meta_data['5. Time Zone']
        )

        # Parse and save the time series data
        time_series_data = data['Time Series (Daily)']
        for date_str, daily_data in time_series_data.items():
            EthereumDaily.objects.create(
                meta_data=meta,
                date=datetime.datetime.strptime(date_str, '%Y-%m-%d').date(),
                open=daily_data['1. open'],
                high=daily_data['2. high'],
                low=daily_data['3. low'],
                close=daily_data['4. close'],
                volume=int(daily_data['5. volume'])
            )


"""
    Some suggestions:

    API Endpoint and Parameters:
        Your API endpoint includes the apikey as part of the URL string.
        Since you are also passing params with 'api_key': alpha_vantage_api_key, ensure that the API expects the key in this format.
        Some APIs require the key as a query parameter (which you've done), but since it's also in the URL, double-check the API documentation for the correct usage.

    Error Handling:
        Consider adding error handling for the network request and the response parsing.
        For instance, check if the response status code is 200 (OK) before parsing the JSON.
        Also, handle possible exceptions like requests.exceptions.RequestException for network-related errors.

    Data Validation:
        Before creating instances of BitcoinDailyMeta and BitcoinDaily, validate the data you receive.
        This includes checking whether the keys you expect in the JSON ('Meta Data', 'Time Series (Daily)', etc.) are present and formatted correctly.

    Logging:
        It might be useful to add logging to your script, especially to record any errors or important information.
        Django has a built-in logging framework that you can utilize.

    Performance Considerations:
        If you're dealing with a large amount of data, consider using bulk creation methods like BitcoinDaily.objects.bulk_create([...]) to reduce the number of database hits.
        However, this requires gathering all the data into a list before making a single database call, which might increase memory usage.

    Testing:
        Before deploying, test the script in a development environment.
        Make sure it handles various edge cases and the data is stored correctly in the database.    
"""