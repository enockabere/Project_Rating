# Generated by Django 3.2.7 on 2021-09-23 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rateApp', '0010_auto_20210923_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
