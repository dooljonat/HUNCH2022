from . import views
from django.urls import path

app_name = "fermentationlab"
urlpatterns = [
    path('', views.index, name='index'),
    path('charts/temperatures/<int:look_back>', views.get_temperatures, name='temperature_data'),
    path('charts/co2levels/<int:look_back>', views.get_co2levels, name='co2_level_data')
]