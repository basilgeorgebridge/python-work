# Generated by Django 2.2.12 on 2021-12-08 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pmtapp', '0024_auto_20211208_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapplyleave',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
