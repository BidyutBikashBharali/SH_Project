from django.urls import path
from django.urls import path
from . import views


urlpatterns = [

    path("", views.SU, name="SignUp"),
    path("SignIn/", views.SI, name="SignIn"),
    path("LogOut/", views.LO, name="LogOut"),
    path("SetUserDetails/", views.SetUserData, name="SUD"),  
    path("Profile/", views.Profile, name="Profile"),
    path("Profile/Post", views.Post, name="Post"),
]