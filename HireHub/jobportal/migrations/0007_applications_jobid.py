# Generated by Django 4.2 on 2023-07-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0006_applications'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='jobid',
            field=models.IntegerField(default=-1),
        ),
    ]
