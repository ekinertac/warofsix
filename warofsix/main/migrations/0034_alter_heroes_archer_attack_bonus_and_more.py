# Generated by Django 4.1.6 on 2023-03-11 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_heroes_userheroes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroes',
            name='archer_attack_bonus',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='archer_defence_bonus',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='cavalry_attack_bonus',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='cavalry_defence_bonus',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='infantry_attack_bonus',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='infantry_defence_bonus',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='monster_attack_bonus',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='monster_defence_bonus',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='pike_attack_bonus',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='pike_defence_bonus',
            field=models.FloatField(default=1.0),
        ),
    ]