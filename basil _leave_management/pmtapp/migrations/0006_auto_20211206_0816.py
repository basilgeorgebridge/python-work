# Generated by Django 2.2.12 on 2021-12-06 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmtapp', '0005_auto_20211206_0526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Phone_number',
            new_name='Phonenumber',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='Profile_pic',
            new_name='Profilepic',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='User_role',
        ),
    ]
