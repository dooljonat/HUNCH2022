from django.contrib import admin

from .models import Temperature, CO2Level, Humidity, PiCameraImage
from . import models

# Register your models here.
admin.site.register(Temperature)
admin.site.register(CO2Level)
admin.site.register(Humidity)

@admin.register(models.PiCameraImage)
class PiCameraImageAdmin(admin.ModelAdmin):
    list_display = ('image_tag',)