# Generated by Django 4.1.6 on 2023-02-22 11:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_usertracker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('is_read', models.BooleanField(default=False)),
                ('sender', models.ManyToManyField(related_name='sender_user', to=settings.AUTH_USER_MODEL)),
                ('target', models.ManyToManyField(related_name='targer_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Mail',
        ),
    ]
