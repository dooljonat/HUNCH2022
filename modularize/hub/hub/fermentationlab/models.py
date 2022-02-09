from django.db import models

# Create your models here.
class Temperature(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    temperature = models.IntegerField()

    class Meta:
        ordering = ['-created_on']

class CO2Level(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    co2_level = models.IntegerField()

    class Meta:
        ordering = ['-created_on']

class Humidity(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    humidity = models.IntegerField()

    class Meta:
        ordering = ['-created_on']