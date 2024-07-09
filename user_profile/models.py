from django.db import models
from django.contrib.auth.models import AbstractUser

from .manage import CustomUserManager
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(max_length=150,unique=True,error_messages={
        "unique":"The Email Must Be Unique !"
    })
    profile_image=models.ImageField(null=True,blank=True,upload_to='profile_image')

    REQUIRED_FIELDS=["email"]
    objects=CustomUserManager
    
    def __str__(self):
        return self.username
    
