# Generated by Django 3.2.7 on 2021-09-23 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rateApp', '0008_auto_20210923_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='profile',
        ),
    ]
