# Generated by Django 3.0.11 on 2020-11-23 23:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201124_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 23, 23, 54, 18, 592973, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='premia',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 23, 23, 54, 18, 592973, tzinfo=utc)),
        ),
    ]
