# Generated by Django 4.1.6 on 2023-02-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_settlement_building_troopupgrades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbuildings',
            name='training_checkout',
        ),
        migrations.RemoveField(
            model_name='userbuildings',
            name='training_time_passed',
        ),
        migrations.RemoveField(
            model_name='userbuildings',
            name='training_troops',
        ),
        migrations.AddField(
            model_name='userbuildings',
            name='resource_worker',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
