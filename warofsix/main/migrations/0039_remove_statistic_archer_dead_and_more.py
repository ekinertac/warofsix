# Generated by Django 4.1.6 on 2023-03-22 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_alter_userheroes_current_health'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistic',
            name='archer_dead',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='archer_kill',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='cavalry_dead',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='cavalry_kill',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='infantry_dead',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='infantry_kill',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='pikeman_dead',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='pikeman_kill',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='siege_dead',
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='siege_kill',
        ),
        migrations.AddField(
            model_name='statistic',
            name='dead',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statistic',
            name='kill',
            field=models.PositiveIntegerField(default=0),
        ),
    ]