# Generated by Django 4.1.6 on 2023-02-14 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_troops_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='troops',
            name='burden',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
