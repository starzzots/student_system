from django.shortcuts import render
from django.contrib.auth.mixins import AccessMixin
from project.settings import *
from students.models import Student
# Create your views here.


def login(request):
    return render(request, 'registration/login.html')


def signup(request):
    return render(request, 'registration/signup.html')
