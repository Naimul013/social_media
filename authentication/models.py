from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField( max_length=50,unique=True)
    email = models.EmailField( max_length=254, unique=True)
    
    mobile_number = models.CharField( max_length=20)
    bio = models.CharField(max_length=100)
    profile_pic = models.ImageField( upload_to='profile_pic/', height_field=None, width_field=None, max_length=None)
    cover_pic = models.ImageField(upload_to='cover_pic/', height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    
    

    
