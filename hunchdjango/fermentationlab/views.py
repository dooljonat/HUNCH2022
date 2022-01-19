from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseNotFound, JsonResponse, HttpResponse

from .models import Temperature, CO2Level
from .utils import lookback_options, colorPrimary, colorSuccess, colorDanger

# Create your views here.


def index(request):
    return render(request, 'fermentationlab/index.html', {})


"""TODO: Make these return temperature and CO2Level
   data in json format, going as far back from the current date as look_back
"""


def get_temperatures(request, look_back):
    if look_back not in lookback_options:
        look_back = 1

    objects = Temperature.objects.all().order_by('-created_on')[:look_back][::-1]
    created_on = []
    temperatures = []
    for x in objects:
        created_on.append(x.created_on)
        temperatures.append(x.temperature)

    return JsonResponse({'title': f'Temperatures in last {look_back} days',
                         'data': {
                             'labels': created_on,
                             'datasets': [{
                                 'label': 'Temperature',
                                 'backgroundColor': colorPrimary,
                                 'borderColor': colorPrimary,
                                 'data': temperatures,
                             }]
                         }, })


def get_co2levels(request, look_back):
    if look_back not in lookback_options:
        look_back = 1

    objects = CO2Level.objects.all().order_by('-created_on')[:look_back][::-1]
    created_on = []
    co2_levels = []
    for x in objects:
        created_on.append(x.created_on)
        co2_levels.append(x.co2_level)

    return JsonResponse({'title': f'CO2Levels in last {look_back} days',
                         'data': {
                             'labels': created_on,
                             'datasets': [{
                                 'label': 'CO2Level',
                                 'backgroundColor': colorPrimary,
                                 'borderColor': colorPrimary,
                                 'data': co2_levels,
                             }]
                         }, })
