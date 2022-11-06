# Generated by Django 4.0.6 on 2022-11-06 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_room_members'),
        ('chat_messages', '0002_alter_message_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='rooms.room'),
        ),
    ]