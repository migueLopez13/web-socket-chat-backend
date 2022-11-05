from django.db import models
from apps.users.models import User


class Room(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE),
    members = models.ManyToManyField(User)
    name = models.CharField(max_length=50),
    background_color = models.CharField(max_length=50),
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
