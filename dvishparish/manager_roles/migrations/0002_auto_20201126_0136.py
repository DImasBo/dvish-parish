# Generated by Django 3.0.11 on 2020-11-25 23:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0004_auto_20201126_0136'),
        ('manager_roles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultdaily',
            name='KPI',
        ),
        migrations.RemoveField(
            model_name='resultdaily',
            name='KPl_result_amount',
        ),
        migrations.CreateModel(
            name='ResultItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KPl_result_amount', models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(1)])),
                ('KPI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results_items', to='plans.KPI')),
                ('result_daily', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results_items', to='manager_roles.ResultDaily')),
            ],
        ),
    ]