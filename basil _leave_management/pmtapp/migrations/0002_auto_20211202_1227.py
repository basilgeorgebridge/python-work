# Generated by Django 2.2.12 on 2021-12-02 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmtapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='User_role',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='designation',
            field=models.CharField(max_length=100),
        ),
    ]