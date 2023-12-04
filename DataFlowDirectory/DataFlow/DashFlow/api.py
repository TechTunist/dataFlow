from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BitcoinDaily, Person
from .serializers import BitcoinDailySerializer, BitcoinDateAndCloseSerializer, PersonSerializer
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
        btc_daily = BitcoinDaily.objects.all()

        serializer = BitcoinDateAndCloseSerializer(btc_daily, many=True)
        return Response(serializer.data)
    

# returns all daily price close number with date
@api_view(['GET'])
def person(request):
    if request.method == 'GET':
        person = Person.objects.all()

        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)