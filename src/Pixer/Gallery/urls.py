from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="gallery"),
    path('toggle-favorite', views.toggle_favorite, name="toggle_favorite"),
    path('image/<str:image_id>', views.image_page, name="image_page"),
    path('page', views.get_page, name="get_page"),
    path('favorites-page', views.get_favorites_page, name="get_favorites_page"),
    path('update', views.update_image_info, name="update_image_info"),
    path('remove', views.remove_gallery, name="remove_gallery"),
    path('download', views.download, name="download_gallery")
]