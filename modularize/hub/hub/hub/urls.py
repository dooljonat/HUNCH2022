"""hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

import core.views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('auth/', include('users.urls'), name='users'),
    path('accounts/profile/', core_views.account_redirect, name="acccount_rediriect"),
    path('fermentationlab/', include('fermentationlab.urls')),
    path('fungilab/', include('fungilab.urls'), name="fungilab")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print(settings.MEDIA_URL)
print(settings.MEDIA_ROOT)