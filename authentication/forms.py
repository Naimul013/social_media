#This module is for all the authentication forms 

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','email','mobile_number','bio','profile_pic','cover_pic')

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username','password')