from http.client import PAYMENT_REQUIRED
from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} (${self.price})"

class Purchase(models.Model):
    customer_full_name = models.CharField(max_length=64)
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    PAYMENT_METHODS = [
        ('CC', 'Credit Card'),
        ('DC', 'Debit Card'),
        ('ET', 'Ethereum'),
        ('BC', 'Bitcoin')
    ]