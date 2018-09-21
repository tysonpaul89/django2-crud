"""
Student Models
"""
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom User Model
    Adding extra fields age to the django's auth model
    """
    school_type = (
        ('ES', 'Elementry School'),
        ('MS', 'Middle School'),
        ('HS', 'High School')
    )
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    gender = models.BooleanField(default=None)
    school = models.CharField(max_length=2, choices=school_type)
