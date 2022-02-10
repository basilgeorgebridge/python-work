# Generated by Django 2.2.12 on 2021-12-08 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmtapp', '0018_auto_20211208_0407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Designation',
            new_name='designation',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='Phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='Profilepic',
            new_name='profilepic',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]