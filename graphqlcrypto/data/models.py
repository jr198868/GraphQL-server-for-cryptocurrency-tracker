from django.db import models

class historicaldata(models.Model):
    name = models.CharField(max_length = 100)
    symbol = models.TextField(blank=True)
    openingprice = models.TextField(blank=True)
    closingprice = models.TextField(blank=True)
    volume = models.TextField(blank=True)