from rest_framework import serializers
from .models import BitcoinDailyMeta, BitcoinDaily, Person

# Bitcoin Serializers
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


# Ethereum Serializers
class EthereumDailyMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitcoinDailyMeta
        fields = ['information', 'symbol', 'last_refreshed', 'output_size', 'time_zone']

class EthereumDailySerializer(serializers.ModelSerializer):
    meta_data = BitcoinDailyMetaSerializer()

    class Meta:
        model = BitcoinDaily
        fields = ['meta_data', 'date', 'open', 'high', 'low', 'close', 'volume']

class EthereumDateAndCloseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitcoinDaily
        fields = ['date', 'close']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'email', 'age', 'phone', 'access']