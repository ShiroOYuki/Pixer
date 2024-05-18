from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="gallery"),
    path('toggle-favorite', views.toggle_favorite, name="toggle_favorite"),
    path('image/<str:image_id>', views.image_page, name="image_page"),
]