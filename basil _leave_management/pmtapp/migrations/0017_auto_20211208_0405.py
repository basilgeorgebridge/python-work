# Generated by Django 2.2.12 on 2021-12-08 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmtapp', '0016_auto_20211208_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapplyleave',
            name='session',
            field=models.CharField(blank=True, max_length=200, verbose_name='half'),
        ),
    ]
