from django.urls import path

from .views import *

urlpatterns = [
    path('post/', savePcData),
    path('get/all/', getAllPcData),
]