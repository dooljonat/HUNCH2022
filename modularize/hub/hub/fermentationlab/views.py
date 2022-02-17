from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime, timedelta

from .models import Humidity, Temperature, CO2Level
from .utils import lookback_options, colorPrimary, colorSuccess, colorDanger
from .forms import DownloadDataForm, model_dict, lookback_dict


def index(request):
    return render(request, 'fermentationlab/index.html', {'user': request.user})


def download_data(request):
    # If this is a POST method we need to process the form data
    if request.method == 'POST':
        form = DownloadDataForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['model_field'])
            model = model_dict.get(form.cleaned_data['model_field'])
            lookback = lookback_dict.get(form.cleaned_data['lookback_field'])
            return HttpResponseRedirect(f'/fermentationlab/charts/{model}/{lookback}')

    # If a GET (or any other method) we'll create a blank form
    else:
        form = DownloadDataForm()

    return render(request, 'fermentationlab/download-data.html', {'form': form})
def image_gallery(request):
    return render(request, 'fermentationlab/image-gallery.html')



def get_lookback_options(request):
    return JsonResponse({
        'options': lookback_options
    })


def get_temperatures(request, look_back):
    if look_back not in lookback_options:
        look_back = 1

    objects = Temperature.objects.filter(
        created_on__gte=datetime.now()-timedelta(days=look_back))
    created_on = []
    temperatures = []
    for x in objects:
        created_on.append(x.created_on.date())
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

    objects = CO2Level.objects.filter(
        created_on__gte=datetime.now()-timedelta(days=look_back))
    created_on = []
    co2_levels = []
    for x in objects:
        created_on.append(x.created_on.date())
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


def get_humidities(request, look_back):
    if look_back not in lookback_options:
        look_back = 1

    objects = Humidity.objects.filter(
        created_on__gte=datetime.now()-timedelta(days=look_back))
    created_on = []
    humidities = []
    for x in objects:
        created_on.append(x.created_on.date())
        humidities.append(x.humidity)

    return JsonResponse({'title': f'Humidity in last {look_back} days',
                         'data': {
                             'labels': created_on,
                             'datasets': [{
                                 'label': 'CO2Level',
                                 'backgroundColor': colorPrimary,
                                 'borderColor': colorPrimary,
                                 'data': humidities,
                             }]
                         }, })
