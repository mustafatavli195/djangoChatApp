from django.urls import path
from . import views

#user_app

urlpatterns = [
    path("" , views.login , name="login"),
    path("register/" , views.register , name="register"),
    path("logout/" , views.logout , name="logout")
]

