from . import views
from django.urls import path

app_name = "fermentationlab"
urlpatterns = [
    path('charts/lookback-options', views.get_lookback_options),
    path('charts/temperatures/<int:look_back>', views.get_temperatures),
    path('charts/co2levels/<int:look_back>', views.get_co2levels)
]
