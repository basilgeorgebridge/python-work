# Generated by Django 2.2.12 on 2021-12-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmtapp', '0008_remove_userprofile_userrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Phonenumber',
            field=models.IntegerField(max_length=100),
        ),
    ]