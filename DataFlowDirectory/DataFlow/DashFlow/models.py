from django.db import models


class BitcoinDailyMeta(models.Model):
    information = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    last_refreshed = models.DateField()
    output_size = models.CharField(max_length=20)
    time_zone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.symbol} - {self.last_refreshed.strftime('%Y-%m-%d')}"


class BitcoinDaily(models.Model):
    meta_data = models.ForeignKey(BitcoinDailyMeta, on_delete=models.CASCADE)
    date = models.DateField()
    open = models.DecimalField(max_digits=15, decimal_places=4)
    high = models.DecimalField(max_digits=15, decimal_places=4)
    low = models.DecimalField(max_digits=15, decimal_places=4)
    close = models.DecimalField(max_digits=15, decimal_places=4)
    volume = models.BigIntegerField()

    def __str__(self):
        return f"{self.meta_data} - {self.date.strftime('%Y-%m-%d')}: Open: {self.open}, Close: {self.close}"

