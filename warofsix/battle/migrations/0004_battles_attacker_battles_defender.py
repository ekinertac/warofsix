# Generated by Django 4.1.6 on 2023-03-26 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('battle', '0003_rename_current_attackerdeads_troop_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='battles',
            name='attacker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attacker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='battles',
            name='defender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='defender', to=settings.AUTH_USER_MODEL),
        ),
    ]
