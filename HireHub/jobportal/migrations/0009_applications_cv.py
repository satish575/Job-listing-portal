# Generated by Django 4.2 on 2023-07-17 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0008_rename_firstname_applications_fullname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='cv',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='cv/'),
        ),
    ]
