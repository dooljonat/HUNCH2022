from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('home.urls')),
    path('fermentationlab', include('fermentationlab.urls'), name="fermentationlab"),
]

urlpatterns += staticfiles_urlpatterns()