from rest_framework.response import Response
from rest_framework.views import APIView
from apps.chat_messages.models import Message
from apps.chat_messages.api.serializers import MessageSerializer


class MessageApiView(APIView):

    def get(self, request):
        messages = Message.objects.all()
        messages_serializer = MessageSerializer(messages, many=True)
        return Response(messages_serializer.data)
