# Generated by Django 3.0.11 on 2020-11-23 23:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0005_auto_20201124_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalplan',
            name='date_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 23, 23, 47, 42, 445154, tzinfo=utc)),
        ),
    ]
