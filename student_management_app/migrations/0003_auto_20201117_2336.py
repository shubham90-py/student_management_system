# Generated by Django 3.0.8 on 2020-11-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0002_auto_20201117_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]