from rest_framework import serializers
from apps.chat_messages.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message()
        fields = '__all__'
