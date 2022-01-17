from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Temperature

# Create your views here.
def index(request):
    return render(request, 'fermentationlab/index.html', {})
