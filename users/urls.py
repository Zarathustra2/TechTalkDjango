from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    
    path("", LandingPageView.as_view(), name="landing"),
    
    path("register/", register, name="register"),
    
    path("profile/", ProfileFormView.as_view(), name="profile"),
    
    # url mit einem Integer als Parameter
    path('profile/<int:user_id>/public/', UserProfileView.as_view(), name="public_profile"),
    
    path('users/list/', UsersListView.as_view(), name="users_list"),
]
