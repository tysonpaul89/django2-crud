"""
Student View Page
"""
from django.shortcuts import render
from .models import CustomUser

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
    # if request.method != 'POST':
    #     pass
    # else:
    #     pass

    return render(request, 'student/create.html')

def edit_student(request, student_id):
    """
    To Update Student
    """
    print(student_id)
    pass

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