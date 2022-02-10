from . import views
from django.urls import path

app_name = "fungilab"
urlpatterns = [
    path('', views.index, name='index'),
]