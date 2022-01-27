from django.contrib import admin
from django.urls import path 
from daksh import views

urlpatterns = [
    path("" , views.index , name = "home"),
    path("signup" , views.signup , name = "signup"),
    path("login" , views.login , name = "login"),
    path("logout" , views.handlelogout , name = "handlelogout"),
    path("about" , views.about , name = "about"),
    path("gallery" , views.gallery , name = "gallery"),
    path("contact" , views.contact , name = "contact"),
    path("join_us" , views.join_us , name = "join_us"),
    path("profile" , views.profile , name = "profile"),
]