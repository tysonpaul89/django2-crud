"""
Student View Page
"""
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from util.db import to_dict

from .models import CustomUser
from .forms import UserForm, GENDER_TYPE, SCHOOL_TYPE

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
    # Initialized form model, if form is submitted then
    # the form data is automatically assigned from POST body
    form = UserForm(request.POST or None)
    # Process form on POST request
    if request.method == 'POST':
        # Validates the form
        if form.is_valid():
            # Saves the user data
            form.save()
            # Adding flash message
            messages.add_message(
                request,
                messages.SUCCESS,
                'Student data added successfully'
            )
            # Redirecting user to listing page
            return redirect('student:list_student')
        else:
            # Adding bootstrap error class to the invalid fields
            for error_field in form.errors:
                if error_field in form.fields:
                    form.fields[error_field].widget.attrs['class'] += ' is-invalid'
    # Renders the form
    return render(request, 'student/create.html', {'form': form})

def edit_student(request, student_id):
    """
    To Update Student
    """
    try:
        # Gets student model
        student = CustomUser.objects.get(pk=student_id)
        # Sets form data with student details
        form = UserForm(request.POST or None, instance=student)
    except CustomUser.DoesNotExist: # If( user not found
        # Redirect user to listing page with flash message
        messages.add_message(
            request,
            messages.ERROR,
            'Student not found!'
        )
        # Redirecting user back to student listing
        return redirect('student:list_student')
    else:
        if request.method == 'POST' and form.is_valid():
            form.save()
            # Setting success flash message
            messages.add_message(
                request,
                messages.SUCCESS,
                'Student data updated successfully'
            )
            # Redirecting user back to student listing
            return redirect('student:list_student')
        else:
            # Adding bootstrap error class to the invalid fields
            for error_field in form.errors:
                if error_field in form.fields:
                    form.fields[error_field].widget.attrs['class'] += ' is-invalid'

        # Renders the edit form
        return render(request, 'student/update.html', {'form':form})

def view_student(request, student_id):
    """
    To View Student Detail
    """
    # Executing raw sql queries
    sql = '''
        SELECT
            `id`,
            `name`,
            `age`,
            `email`,
            `gender`,
            `school`,
            `is_active`
        FROM
            `student_customuser`
        WHERE
            `id` = %s
        '''
    cursor = connection.cursor()
    # Binding params, so that django will filter its value to prevent sql injection
    cursor.execute(sql, [student_id])
    # Executing query
    result = cursor.fetchone()
    # Converting query results into dictionary containing column name as keys
    user_data = to_dict(cursor, result)
    # Rending template
    return render(request, 'student/view.html', {
        'user_data': user_data,
        'gender_data': dict(GENDER_TYPE),
        'school_data': dict(SCHOOL_TYPE)
    })

def delete_student(request, student_id):
    """
    To Delete Student
    """
    try:
        # Deletes user data
        CustomUser.objects.get(pk=student_id).delete()
        # Sets flash mesage
        messages.add_message(
            request,
            messages.INFO,
            'Student data deleted successfully'
        )
    except CustomUser.DoesNotExist: # If user not found
        # Sets flash mesage
        messages.add_message(
            request,
            messages.ERROR,
            'Student not found!'
        )
    # Redirect user to student listing page
    return redirect('student:list_student')
