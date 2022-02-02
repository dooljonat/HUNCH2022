from django.contrib import admin

from .models import Temperature, CO2Level, Humidity

# Register your models here.
admin.site.register(Temperature)
admin.site.register(CO2Level)
admin.site.register(Humidity)
