from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators import gzip
from django.http import HttpResponseNotFound, JsonResponse, HttpResponse, StreamingHttpResponse
from datetime import datetime, timedelta

from .models import Temperature, CO2Level
from .utils import lookback_options, colorPrimary, colorSuccess, colorDanger
# from .camera import VideoCamera


def index(request):
    return render(request, 'core/index.html', {})

# @gzip.gzip_page
# def video_stream(request):
#     try:
#         cam = VideoCamera()
#         return StreamingHttpResponse(gen_frames(cam), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:
#         pass

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

# # Reading video feed
# def gen_frames(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                 b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')