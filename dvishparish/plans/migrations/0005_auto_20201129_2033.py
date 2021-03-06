# Generated by Django 3.0.11 on 2020-11-29 18:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0004_auto_20201129_0419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='managerplan',
            name='KPI',
        ),
        migrations.RemoveField(
            model_name='managerplan',
            name='general_plan',
        ),
        migrations.RemoveField(
            model_name='managerplan',
            name='user',
        ),
        migrations.AlterField(
            model_name='generalplan',
            name='date_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 18, 33, 38, 138826, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='date_from',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 18, 33, 38, 138204, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='BankOfficePlan',
        ),
        migrations.DeleteModel(
            name='ManagerPlan',
        ),
    ]
