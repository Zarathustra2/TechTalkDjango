# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# IMPORTIER MICH
from django.views import View
from django.views.generic import TemplateView, ListView

from users.forms import RegistrationForm, ProfileForm
from users.models import Profile


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
            
            return HttpResponseRedirect(reverse('users:landing'))
    
    return render(request, 'users/register.html', {'form': form})


class ProfileFormView(View):
    template_name = "users/profile.html"
    
    def get(self, request, *args, **kwargs):
        user = self.get_user(request)
        profile = Profile.objects.filter(user=user)
        if profile:
            form = ProfileForm(instance=profile[0])
        else:
            form = ProfileForm()
        
        return self.render({'form_1': form})
    
    def post(self, request, *args, **kwargs):
        profile, created = Profile.objects.get_or_create(user=self.get_user(request))
        
        form = ProfileForm(data=request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return self.render({'form_1': form, 'update': True})
    
    def render(self, context):
        return render(self.request, self.template_name, context)
    
    def get_user(self, request):
        return self.request.user


class UserProfileView(View):
    
    def get(self, request, *args, **kwargs):
        user_id = self.get_user_id(**kwargs)
        
        model = get_object_or_404(Profile, user=get_object_or_404(User, pk=user_id))
        
        return render(request, 'users/public_profile.html', {'profile': model})
    
    def get_user_id(self, **kwargs):
        # URL Parameter werden bei Class-Based-Views in die **kwargs gepackt.
        return kwargs.get('user_id', False)


class UsersListView(ListView):
    """
        Generic List View. Diese View ist schon von Django implementiert.
        Diese View übergibt dann alle Objekte eines Models an das Template
    """
    
    # Model
    model = User
    
    # Ändern des Paramternamen im Template, siehe for-loop im Template
    context_object_name = 'users'
    
    # Template
    template_name = 'users/users_list.html'
