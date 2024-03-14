from django.core.management.base import BaseCommand
import requests
from DashFlow.models import EthereumDailyMeta, EthereumDaily
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class Command(BaseCommand):
    help = "Fetches and stores Ethereum daily data"

    def handle(self, *args, **kwargs):
        api_endpoint = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=ETHUSD&apikey={}".format(os.getenv('ALPHA_VANTAGE_API_KEY'))
        response = requests.get(api_endpoint)
        data = response.json()

        # Assuming meta_data remains fairly constant, otherwise use get_or_create or update_or_create as needed
        meta_data = data['Meta Data']
        meta, created = EthereumDailyMeta.objects.get_or_create(
            symbol=meta_data['2. Symbol'],
            defaults={
                'information': meta_data['1. Information'],
                'last_refreshed': datetime.datetime.strptime(meta_data['3. Last Refreshed'], '%Y-%m-%d').date(),
                'output_size': meta_data['4. Output Size'],
                'time_zone': meta_data['5. Time Zone']
            }
        )

        # Parse and save the time series data
        time_series_data = data['Time Series (Daily)']
        for date_str, daily_data in time_series_data.items():
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            EthereumDaily.objects.update_or_create(
                meta_data=meta,
                date=date_obj,
                defaults={
                    'open': daily_data['1. open'],
                    'high': daily_data['2. high'],
                    'low': daily_data['3. low'],
                    'close': daily_data['4. close'],
                    'volume': int(daily_data['5. volume'])
                }
            )
