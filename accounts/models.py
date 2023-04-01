from django.contrib.auth.models import AbstractUser 
from django.db import models

# Create your models here.
# 1차원적 
# class User(models.Model):
#     pass 

class User(AbstractUser):
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    # pass 

# class Profile(models.Model):
#     pass 