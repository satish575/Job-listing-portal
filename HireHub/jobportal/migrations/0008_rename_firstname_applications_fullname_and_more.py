# Generated by Django 4.2 on 2023-07-16 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0007_applications_jobid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applications',
            old_name='firstname',
            new_name='fullname',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='lastname',
            new_name='username',
        ),
    ]