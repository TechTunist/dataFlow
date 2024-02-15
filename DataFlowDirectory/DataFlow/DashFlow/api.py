from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BitcoinDaily, EthereumDaily, Person
from .serializers import BitcoinDailySerializer, BitcoinDateAndCloseSerializer, EthereumDailySerializer, EthereumDateAndCloseSerializer
from django.http import HttpResponse


@api_view(['GET'])
def btc_all_data(request):
    try:
        btc_daily = BitcoinDaily.objects.all()
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BitcoinDailySerializer(btc_daily, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def eth_all_data(request):
    try:
        eth_daily = EthereumDaily.objects.all()
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EthereumDailySerializer(eth_daily, many=True)
        return Response(serializer.data)


# returns price data on the given date in the url (eg. '2022-01-01') 
@api_view(['GET'])
def btc_price_by_date(request, start_date):
    if request.method == 'GET':
        # btc_daily = BitcoinDaily.objects.all()

        btc_daily = BitcoinDaily.objects.filter(date=start_date)

        serializer = BitcoinDateAndCloseSerializer(btc_daily, many=True)
        return Response(serializer.data)


# returns all daily price close number with date
@api_view(['GET'])
def btc_price_all(request):
    if request.method == 'GET':
        btc_daily = BitcoinDaily.objects.all().order_by('date')

        serializer = BitcoinDateAndCloseSerializer(btc_daily, many=True)
        return Response(serializer.data)


# returns all daily price close number with date
@api_view(['GET'])
def eth_price_all(request):
    if request.method == 'GET':
        eth_daily = EthereumDaily.objects.all().order_by('date')

        serializer = EthereumDateAndCloseSerializer(eth_daily, many=True)
        return Response(serializer.data)
    

# returns all info related to a person
@api_view(['GET'])
def person(request):
    if request.method == 'GET':
        person = Person.objects.all()

        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)