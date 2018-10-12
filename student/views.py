"""
Student View Page
"""
from django.shortcuts import render, redirect, reverse
from .models import CustomUser
from .forms import UserForm, GENDER_TYPE, SCHOOL_TYPE
from django.db import connection
from util.db import to_dict

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
            form.save()
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
    print(dict(SCHOOL_TYPE))
    print(dict(GENDER_TYPE))
    return render(request, 'student/view.html', {
        'user_data': user_data,
        'gender_data': dict(GENDER_TYPE),
        'school_data': dict(SCHOOL_TYPE)
    })

def delete_student(request, student_id):
    """
    To Delete Student
    """
    pass
