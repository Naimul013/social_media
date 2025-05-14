#This module is for all the authentication forms 

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from social.models import *
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','email','mobile_number','bio','profile_pic','cover_pic')

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username','password')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','mobile_number','bio','profile_pic','cover_pic')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content','image',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
