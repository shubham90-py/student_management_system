# Generated by Django 3.0.8 on 2020-12-03 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_auto_20201125_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='fcm_token',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='students',
            name='fcm_token',
            field=models.TextField(default=' '),
        ),
    ]
