# Generated by Django 2.0 on 2018-10-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chitfund', '0002_auto_20181026_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allotment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, unique_for_month=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]