# Generated by Django 3.0.11 on 2020-11-24 00:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20201124_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 24, 0, 39, 54, 312193, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='premia',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 24, 0, 39, 54, 312193, tzinfo=utc)),
        ),
    ]