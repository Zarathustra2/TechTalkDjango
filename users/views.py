# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'users/homepage.html'


def landing_page(request):
    return render(request, 'users/homepage.html')
