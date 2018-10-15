"""
Account View
"""
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from student.models import CustomUser

from .forms import LoginForm, SignupForm

def login(request):
    """
    Login Page
    """
    form = LoginForm(request.POST or None)
    # try:
    #     data = form.cleaned_data
    #     user = CustomUser.objects.get(email=data['email'])
    #     if user:
    #         authenticate(request, email=user.email, password=user.password)
    # except CustomUser.DoesNotExist:
    #     pass
    # else:
    #     pass
    #     # if form.is_valid():
    # else:
    #     # Adding bootstrap error class to the invalid fields
    #     for error_field in form.errors:
    #         if error_field in form.fields:
    #             form.fields[error_field].widget.attrs['class'] += ' is-invalid'
    return render(request, 'account/login.html', {'form': form})

def signup(request):
    """
    User Signup Page
    """
    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.password = make_password(form.cleaned_data['password'])
            print(form.password)
            form.save()
            return redirect('account:login')
        else:
            # Adding bootstrap error class to the invalid fields
            for error_field in form.errors:
                if error_field in form.fields:
                    form.fields[error_field].widget.attrs['class'] += ' is-invalid'
    return render(request, 'account/signup.html', {'form': form})

def logout(request):
    """
    Logout Page
    """
    return redirect('student:list_student')
