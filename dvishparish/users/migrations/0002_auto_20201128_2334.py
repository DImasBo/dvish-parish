# Generated by Django 3.0.11 on 2020-11-28 21:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 21, 34, 22, 496165, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='premium',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 28, 21, 34, 22, 496165, tzinfo=utc)),
        ),
    ]
