from django.conf import settings 
from django.contrib.auth.models import AbstractUser 
from django.db import models
#from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.validators import RegexValidator

class User(AbstractUser):
    # django3 
    class GenderChoices(models.TextChoices):
        male = "M", "남성"
        female = "F", "여성"
    
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, blank=True, validators=[RegexValidator(r"^010[1-9]\d{3}-?\d{4}$")])
    gender = models.CharField(max_length=1, blank=True, choices=GenderChoices.choices)
    
    def send_welcome_email(self):
        subject = render_to_string("accounts/welcome_email_subject.txt", {
            "user":self,
            
        })
        content = render_to_string("accounts/welcome_email_content.txt", {
            "user":self,
            
        })
        #sender_email = settings.WELCOME_EMAL_SENDER
        #send_mail(subject, content, sender_email, [self.email], faile_silently=False)
        
        
        