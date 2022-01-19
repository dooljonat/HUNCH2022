from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Temperature, CO2Level

# Create your views here.
def index(request):
    return render(request, 'fermentationlab/index.html', {})


"""TODO: Make these return temperature and CO2Level
   data in json format, going as far back from the current date as look_back
"""
def get_temperatures(request, look_back):
    pass

def get_co2levels(request, look_back):
    pass
