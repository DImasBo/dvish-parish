# Generated by Django 3.0.11 on 2020-12-04 11:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0006_auto_20201130_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalplan',
            name='date_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 4, 11, 24, 58, 595226, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='date_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 4, 11, 24, 58, 594626, tzinfo=utc)),
        ),
    ]
