from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms


class RegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username',]
