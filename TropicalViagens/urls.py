"""TropicalViagens URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from apps.latam import views
from django.conf.urls import url

from apps.latam.views import ComputerViewSets, CadastrosViewSets

router = routers.DefaultRouter()
router.register(r'computadores', viewset=ComputerViewSets)
router.register(r'cadastros', viewset=CadastrosViewSets)


urlpatterns = [
    url('api/latam/pagamento', views.pagamento),
    url('api/latam/total', views.total),
    url('', include(router.urls)),
    # url('api/latam/computadores', views.ComputerViewSets),
]
