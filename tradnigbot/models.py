from django.db import models

# Create your models here.

class Currency(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)
    usd_value = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)