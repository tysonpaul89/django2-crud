"""
Student View Page
"""
from django.shortcuts import render, redirect, reverse
from .models import CustomUser
from .forms import UserForm

def list_student(request):
    """
    To List Students
    """
    students = CustomUser.objects.all()

    return render(request, 'student/list.html', {
        'students': students
    })

def create_student(request):
    """
    To Create New Student
    """
    # Process form on POST request
    if request.method == 'POST':
        form = UserForm(request.POST)
        # Validates the form
        if form.is_valid():
            # Saves the user data
            #form.save()
            # Redirecting user to listing page
            return redirect('student:list_student')
        else:
            # Adding bootstrap error class to the invalid fields
            for error_field in form.errors:
                if error_field in form.fields:
                    form.fields[error_field].widget.attrs['class'] += ' is-invalid'
    else:
        # Initializing form on GET request
        form = UserForm()
    return render(request, 'student/create.html', {'form': form})

def edit_student(request, student_id):
    """
    To Update Student
    """
    print(student_id)

def view_student(request, student_id):
    """
    To View Student Detail
    """
    pass

def delete_student(request, student_id):
    """
    To Delete Student
    """
    pass
