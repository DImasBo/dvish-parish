# Generated by Django 3.0.11 on 2020-11-29 02:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0003_auto_20201128_2340'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='KPIitems',
            new_name='KPIitem',
        ),
        migrations.AlterField(
            model_name='generalplan',
            name='date_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 2, 19, 39, 593529, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='date_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 2, 19, 39, 592902, tzinfo=utc)),
        ),
    ]
