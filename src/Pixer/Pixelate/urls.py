from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="pixelate"),
    path('upload', views.process_image, name="process_image"),
    path('test', views.test, name="test"),
    path('pixelate_page', views.pixelate, name="pixelate_page"),
    path('upload-gallery', views.upload_gallery, name="upload_to_gallery")
]