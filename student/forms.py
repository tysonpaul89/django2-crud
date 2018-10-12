"""
Student Form Models
"""
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser, GENDER_TYPE, SCHOOL_TYPE
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
        # Since we are using Django's User model, we only need to show the fields that are
        # needed for our use
        fields = ['name', 'age', 'email', 'gender', 'school', 'is_active']
        # To customize form field attributes
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Age'
            }),
            'gender': forms.RadioSelect(
                attrs={'class': 'form-check-input'},
                choices=GENDER_TYPE
            ),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email'
            }),
            'school': forms.Select(
                attrs={'class':'form-control', 'required': True},
                choices=SCHOOL_TYPE,
            ),
            'is_active': forms.CheckboxInput(
                attrs={'class':'form-check-input'},
            ),
        }
        # To show help text in form fields
        help_texts = {
            'name': 'Please enter your full name',
            'is_active': 'Untick this checkbox to disable the student',
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # Overriding default choice value '-----' to a string
        # Ref: https://stackoverflow.com/questions/12984013/how-to-change-empty-label-for-modelform-choice-field/14032358#14032358
        self.fields["school"].choices = [("", "Please choose a school"),]\
        + list(self.fields["school"].choices)[1:]

    def clean(self):
        # Gets the cleaned data
        cd = super(UserForm, self).clean()

        # To raise non field error
        # raise ValidationError('Non Field Test error')

        # Age Validation
        if cd['age'] < 5:
            raise ValidationError({
                'age': ValidationError(
                    "Age is invalid, Student must be least 5 year old or greater"
                )
            })
        return self.cleaned_data
