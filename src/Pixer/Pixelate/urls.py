from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="pixelate"),
    path('test', views.test, name="test")
]