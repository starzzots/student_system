# Generated by Django 4.1.1 on 2022-09-24 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_students_gpa'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]
