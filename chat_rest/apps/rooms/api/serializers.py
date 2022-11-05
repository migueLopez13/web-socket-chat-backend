from rest_framework import serializers
from apps.rooms.models import Room
from apps.chat_messages.api.serializers import MessageSerializer


class RoomSerializer(serializers.ModelSerializer):
    message = MessageSerializer(many=True)

    class Meta:
        model = Room
        fields = '__all__'
