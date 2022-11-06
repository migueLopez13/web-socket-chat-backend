from django.db import models
from apps.rooms.models import Room
from apps.users.models import User


class Message(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='message_owner',
        on_delete=models.CASCADE
    )
    text = models.CharField('text', blank=True, null=True, max_length=500)
    room = models.ForeignKey(
        Room,
        related_name='messages',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
