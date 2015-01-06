from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

# Create your models here.

class AccountManager(BaseUserManager):
    
    def _create_user(self, username, email, password,
                     is_admin, **extra_fields):
        """
        Creates a user with the given credentials
        """   
        now = timezone.now()
        
        if not email:
            raise ValueError("Must provide a valid email address")
        if not username:
            raise ValueError("Must provide a username")
    
        email = self.normalize_email(email)
        
        user = self.model(
            username = username, email = email, is_admin = is_admin, created_on = now
        )
        user.set_password(password)
        user.save()
        
        return user
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Create a regular (non-admin) user
        """
        return self._create_user(username, email, password, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        """
        Create an admin
        """
        return self._create_user(username, email, password, True, **extra_fields)

class Account(AbstractBaseUser):
    
    username = models.CharField(max_length = 50, unique = True)
    email = models.EmailField(unique = True)
    
    first_name = models.CharField(max_length = 60, blank = True)
    last_name = models.CharField(max_length = 60, blank = True)
    city = models.CharField(max_length = 100, blank = True)
    country = models.CharField(max_length = 100, blank = True)
    
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    
    created_on = models.DateTimeField(auto_now_add = True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = AccountManager()
    
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
        
    def __unicode__(self):
        return self.username

