# Generated by Django 2.2.12 on 2021-12-08 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pmtapp', '0021_remove_userprofile_empid'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapplyleave',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
