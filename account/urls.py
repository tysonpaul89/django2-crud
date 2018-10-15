"""
Account Routes used for authentication
"""
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # /auth/login
    path('login/', views.login, name='login'),
    # /auth/signup
    path('singup/', views.signup, name='singup'),
    # /auth/logout
    path('logout/', views.logout, name='logout'),
]
