from django.db import models
from apps.users.models import User


class Room(models.Model):
    admin = models.ForeignKey(
        User,
        related_name='room_admin',
        on_delete=models.CASCADE
    )
    members = models.ManyToManyField(User, related_name='rooms')
    name = models.CharField('name', blank=True, null=True, max_length=100)
    background_color = models.CharField('background', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
