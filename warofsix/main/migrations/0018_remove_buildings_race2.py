# Generated by Django 4.1.6 on 2023-02-24 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_buildings_race2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buildings',
            name='race2',
        ),
    ]