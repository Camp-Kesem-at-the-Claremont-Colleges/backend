from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model"""

    def create_user(self, username, first_name, last_name, camp_name, role, password):
        """Creates a new user profile object."""

        user = self.model(username=username, first_name=first_name, last_name=last_name, camp_name=camp_name, role=role)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_staffuser(self, username, first_name, last_name, camp_name, role, password):

        user = self.create_user(username, first_name, last_name, camp_name, role, password)
        user.is_staff = True

        user.save(using=self.db)

        return user

    def create_superuser(self, username, first_name, last_name, camp_name, role, password):

        user = self.create_user(username, first_name, last_name, camp_name, role, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self.db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile inside our app"""

    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    camp_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='profiles', blank=True)
    bio = models.CharField(max_length=500, blank=True)
    role = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['camp_name', 'first_name', 'last_name', 'role']

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""
        
        return self.camp_name