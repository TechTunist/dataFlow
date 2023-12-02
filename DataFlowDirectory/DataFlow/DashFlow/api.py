from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BitcoinDaily
from .serializers import BitcoinDailySerializer, BitcoinDateAndCloseSerializer
from django.http import HttpResponse


@api_view(['GET'])
def price(request):
    try:
        btc_daily = BitcoinDaily.objects.all()
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BitcoinDailySerializer(btc_daily, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def price_by_date(request):
    if request.method == 'GET':
        btc_daily = BitcoinDaily.objects.all()
        serializer = BitcoinDateAndCloseSerializer(btc_daily, many=True)
        return Response(serializer.data)