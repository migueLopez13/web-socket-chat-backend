from rest_framework import serializers
from apps.rooms.models import Room
from apps.chat_messages.api.serializers import MessageRelationSerializer
from apps.users.api.serializers import UserRelationSerializer


class RoomSerializer(serializers.ModelSerializer):
    messages = MessageRelationSerializer(many=True)
    members = UserRelationSerializer(many=True)
    admin = UserRelationSerializer(many=False)

    class Meta:
        model = Room
        fields = '__all__'


class RoomRelationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id', 'name']
