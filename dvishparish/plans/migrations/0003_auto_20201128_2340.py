# Generated by Django 3.0.11 on 2020-11-28 21:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_auto_20201128_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalplan',
            name='date_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 21, 40, 35, 66538, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='date_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 21, 40, 35, 65512, tzinfo=utc)),
        ),
    ]
