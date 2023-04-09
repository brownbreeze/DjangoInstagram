from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.core.mail import send_mail


class User(AbstractUser):
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    
    def send_welcome_email(self):
        #title = ""
        
        pass
        
        