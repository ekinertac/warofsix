# Generated by Django 4.1.6 on 2023-02-19 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_troops_training_time_usertroops_last_chekout_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertroops',
            old_name='last_chekout',
            new_name='last_checkout',
        ),
    ]