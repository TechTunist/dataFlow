from rest_framework import serializers
from .models import BitcoinDailyMeta, BitcoinDaily

class BitcoinDailyMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitcoinDailyMeta
        fields = ['information', 'symbol', 'last_refreshed', 'output_size', 'time_zone']

class BitcoinDailySerializer(serializers.ModelSerializer):
    meta_data = BitcoinDailyMetaSerializer()

    class Meta:
        model = BitcoinDaily
        fields = ['meta_data', 'date', 'open', 'high', 'low', 'close', 'volume']

class BitcoinDateAndCloseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitcoinDaily
        fields = ['date', 'close']