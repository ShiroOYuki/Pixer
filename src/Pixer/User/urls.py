from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="user"),
<<<<<<< Updated upstream
    path('create', views.create_user, name="create_user"),
    path('login', views.user_login, name="login"),
    path('update', views.update_user, name="update_user"),
    path('data', views.get_user_data, name="get_user_data")
=======
    path('login', views.login_page, name="login")
>>>>>>> Stashed changes
]