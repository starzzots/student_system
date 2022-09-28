from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Teacher(models.Model):
    teachers_first_name = models.CharField(max_length=50)
    teachers_last_name = models.CharField(max_length=50)
    school_work_for = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
