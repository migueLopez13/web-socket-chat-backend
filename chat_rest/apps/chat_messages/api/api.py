from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.chat_messages.models import Message
from apps.chat_messages.api.serializers import MessageSerializer


@api_view(['GET', 'POST'])
def message_api_view(request):

    if request.method == 'GET':
        messages = Message.objects.all()
        messages_serializer = MessageSerializer(messages, many=True)
        return Response(messages_serializer.data)

    elif request.method == 'POST':
        message_serializer = MessageSerializer(data=request.data)
        if message_serializer.is_valid():
            message_serializer.save()
            return Response(message_serializer.data)
        return Response(message_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def message_detail_api_view(request, pk=None):

    if request.method == 'GET':
        message = Message.objects.filter(id=pk).first()
        message_serializer = MessageSerializer(message)
        return Response(message_serializer.data)

    elif request.method == 'PUT':
        message = Message.objects.filter(id=pk).first()
        message_serializer = MessageSerializer(message, data=request.data)
        if message_serializer.is_valid():
            message_serializer.save()
            return Response(message_serializer.data)
        return Response(message_serializer.errors)

    elif request.method == 'DELETE':
        message = Message.objects.filter(id=pk).first()
        user.delete()
        return Response('deleted')
