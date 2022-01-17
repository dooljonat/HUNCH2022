from django.contrib import admin
from .models import Temperature, CO2Level

# Register your models here.
admin.site.register(Temperature)
admin.site.register(CO2Level)