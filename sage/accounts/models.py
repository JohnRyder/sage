from django.contrib.auth import AbstractBaseUser
from django.db import models

# Create your models here.

class Account(AbstractBaseUser):
    username = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    city = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    
    isAdmin = models.BooleanField(default = False)
    
    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.username
    
    def get_short_name(self):
        if self.first_name:
            return self.first_name
        else:
            return self.username

