# Generated by Django 2.2.12 on 2021-12-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmtapp', '0022_userapplyleave_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]