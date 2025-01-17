# Generated by Django 4.1.6 on 2023-02-23 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0015_remove_messages_sender_remove_messages_target_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='archer_dead',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='archer_kill',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='cavalry_dead',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='cavalry_kill',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='infantry_dead',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='infantry_kill',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='pikeman_dead',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='pikeman_kill',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='siege_dead',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='siege_kill',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settlement_id', models.IntegerField()),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.userbuildings')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
