# Generated by Django 3.0.11 on 2020-11-18 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201118_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='office',
            new_name='bankoffice',
        ),
    ]
