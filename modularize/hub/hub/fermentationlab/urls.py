from . import views
from django.urls import path

app_name = "fermentationlab"
urlpatterns = [
    path('', views.index, name='index'),
    path('download-data/', views.download_data, name='download-data'),
    path('charts/lookback-options', views.get_lookback_options),
    path('charts/temperatures/<int:look_back>', views.get_temperatures),
    path('charts/co2levels/<int:look_back>', views.get_co2levels),
    path('charts/humidities/<int:look_back>', views.get_humidities)
]