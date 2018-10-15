"""
Student Form Models
"""
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from student.models import CustomUser
from django.forms import ModelForm, ValidationError

class SignupForm(ModelForm):
    # Custom form field for confirm password
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password'
        })
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

        # To customize form field attributes
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email'
            }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Password'
                }
            ),
        }

    def clean(self):
        # Gets the cleaned data
        cd = super(SignupForm, self).clean()

        # Password validation
        if cd['password'] != cd['password1']:
            raise ValidationError({
                'password': ValidationError(
                    "Password doesn't match!"
                )
            })
        elif len(cd['password']) < 8:
            raise ValidationError({
                'password': ValidationError(
                    "Password must be at least 8 character long"
                )
            })

        try:
            user = CustomUser.objects.get(email=cd['email'])
            if user:
                raise ValidationError({
                    'email': ValidationError(
                        'This email is registered!'
                    )
                })
        except CustomUser.DoesNotExist:
            pass

        return self.cleaned_data

class LoginForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

        # To customize form field attributes
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email'
            }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Password'
                }
            )
        }