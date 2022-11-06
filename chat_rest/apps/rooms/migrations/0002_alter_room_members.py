# Generated by Django 4.0.6 on 2022-11-06 08:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='members',
            field=models.ManyToManyField(related_name='room_members', to=settings.AUTH_USER_MODEL),
        ),
    ]
