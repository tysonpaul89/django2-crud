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
    # Overrides the django's user model email field and made it unique
    # to replace USERNAME_FIELD as email.
    # This is done bcoz we don't want to use username field in the site
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    name = models.CharField(max_length=100, default='')
    age = models.PositiveIntegerField(default=0)
    # We are going to show this gender field as a radio button. For this we set the
    # value for the 'default' argument and 'blank=False' so that django doesn't
    # include the blank choice '-----' in the from
    # Ref: https://stackoverflow.com/questions/42390311/remove-blank-from-radioselect/42401631#42401631
    gender = models.CharField(
        max_length=1,
        choices=GENDER_TYPE,
        default=GENDER_TYPE[0][0],
        blank=False
    )
    school = models.CharField(
        max_length=2,
        choices=SCHOOL_TYPE,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)

    # Overriding username field and setting it as a none unique field bcoz
    # we don't want to use usernam in the site instead we want to use email for that
    username = models.CharField(max_length=40, unique=False, default='')
    # Setting email field as replacement to username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'age', 'gender', 'school', 'is_active']

    def __str__(self):
        return self.email
