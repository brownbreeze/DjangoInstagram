from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User 


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields['email'].required)
        
        self.fields['email'].required = True 
        self.fields['first_name'].required = True 
        self.fields['last_name'].required = True 
        
    class Meta(UserCreationForm.Meta):
        model = User 
        fields = ['username', 'email', 'first_name', 'last_name']
    