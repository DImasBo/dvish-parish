# Generated by Django 3.0.11 on 2020-11-26 00:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0007_auto_20201126_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalplan',
            name='date_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 0, 52, 47, 270740, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='date_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 26, 0, 52, 47, 270035, tzinfo=utc)),
        ),
    ]
