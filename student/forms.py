"""
Student Form Models
"""
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
from django.forms import ModelForm, ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'age', 'gender', 'school', 'is_active']
    def clean_name(self):
        raise ValidationError('Test error')