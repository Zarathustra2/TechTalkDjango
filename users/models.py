from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    TRACK_CHOICES = [
        ('Elektro', 'Elektrotechnik'),
        ('Info', 'Informatik'),
        ('Wi-info', 'Wirtschaftsinformatik'),
        ('T-Info', 'Theoretische Inforamtik')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    description = models.TextField()
    
    track = models.CharField(max_length=25, default='Info', choices=TRACK_CHOICES)
    semester = models.PositiveIntegerField(default=1)
    
    created = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('users:public_profile', kwargs={'user_id': self.user.id})
