from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    
    path("", LandingPageView.as_view(), name="landing"),
    
    path("register/", register, name="register"),
    
]







