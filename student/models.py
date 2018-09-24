"""
Student Models
"""
from django.db import models
from django.contrib.auth.models import AbstractUser

SCHOOL_TYPE = (
    ('ES', 'Elementry School'),
    ('MS', 'Middle School'),
    ('HS', 'High School')
)
GENDER_TYPE = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class CustomUser(AbstractUser):
    """
    Custom User Model
    Adding extra fields age to the django's auth model
    """
    name = models.CharField(max_length=100, default='')
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_TYPE,
        null=True,
        blank=True
    )
    school = models.CharField(
        max_length=2,
        choices=SCHOOL_TYPE,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)
