# Generated by Django 3.0.11 on 2020-11-23 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager_roles', '0001_initial'),
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultdaily',
            name='KPI',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results_daily', to='plans.KPI'),
        ),
    ]