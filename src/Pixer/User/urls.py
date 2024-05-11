from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="user"),
    path('create', views.create_user, name="create_user"),
    path('login', views.user_login, name="login")
]