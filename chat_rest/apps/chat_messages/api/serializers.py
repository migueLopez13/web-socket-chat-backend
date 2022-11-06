from rest_framework import serializers
from apps.chat_messages.models import Message
from apps.users.api.serializers import UserOwnerSerializer


class MessageSerializer(serializers.ModelSerializer):
    owner = UserOwnerSerializer(many=False)

    class Meta:
        model = Message()
        fields = '__all__'


class MessageRelationSerializer(serializers.ModelSerializer):
    owner = UserOwnerSerializer(many=False)

    class Meta:
        model = Message()
        fields = ['id', 'owner', 'text', 'created_at', 'updated_at']
