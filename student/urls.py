"""
Student Routes
"""
from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    # /
    path('', views.list_student, name='list_student'),
    # /create
    path('create/', views.create_student, name='create_student'),
    # /edit/1
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    # /view/1
    path('view/<int:student_id>/', views.view_student, name='view_student'),
    # /delete/1
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
]
