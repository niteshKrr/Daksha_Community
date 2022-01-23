from django.contrib import admin
from django.urls import path 
from daksh import views

urlpatterns = [
    path("" , views.index , name = "home"),
    path("about" , views.about , name = "about"),
    path("galary" , views.galary , name = "galary"),
    path("contact" , views.contact , name = "contact"),
    path("join_us" , views.join_us , name = "join_us"),
    path("signup" , views.signup , name = "signup"),
    path("login" , views.login , name = "login"),
    path("logout" , views.logout , name = "logout"),
    path("profile" , views.profile , name = "profile"),
]