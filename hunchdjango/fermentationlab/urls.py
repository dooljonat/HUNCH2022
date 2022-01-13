from . import views
from django.urls import path

app_name = "fermentationlab"
urlpatterns = [
    path('', views.index, name='index'),
]