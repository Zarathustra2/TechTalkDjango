# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import TemplateView

from users.forms import RegistrationForm


class LandingPageView(TemplateView):
    template_name = 'users/homepage.html'


def landing_page(request):
    return render(request, 'users/homepage.html')


def register(request):
    if request.method != 'POST':
        
        form = RegistrationForm()
    else:
        form = RegistrationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            
            login(request, new_user)
    
    return render(request, 'users/register.html', {'form': form})