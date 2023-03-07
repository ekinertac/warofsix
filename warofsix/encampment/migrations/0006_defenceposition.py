# Generated by Django 4.1.6 on 2023-03-04 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0031_alter_buildings_race_alter_troops_race'),
        ('encampment', '0005_departingtroops_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefencePosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('percent', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_troop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.usertroops')),
            ],
        ),
    ]
