# Generated by Django 3.0.8 on 2020-11-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancereport',
            name='update_at',
        ),
        migrations.AddField(
            model_name='attendancereport',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
