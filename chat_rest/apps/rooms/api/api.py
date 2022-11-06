from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.rooms.models import Room
from apps.rooms.api.serializers import RoomSerializer


@api_view(['GET', 'POST'])
def room_api_view(request):

    if request.method == 'GET':
        rooms = Room.objects.all()
        rooms_serializer = RoomSerializer(rooms, many=True)
        return Response(rooms_serializer.data)

    elif request.method == 'POST':
        room_serializer = RoomSerializer(data=request.data)
        if room_serializer.is_valid():
            room_serializer.save()
            return Response(room_serializer.data)
        return Response(room_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def room_detail_api_view(request, pk=None):

    if request.method == 'GET':
        room = Room.objects.filter(id=pk).first()
        room_serializer = RoomSerializer(room)
        return Response(room_serializer.data)

    elif request.method == 'PUT':
        room = Room.objects.filter(id=pk).first()
        room_serializer = RoomSerializer(room, data=request.data)
        if room_serializer.is_valid():
            room_serializer.save()
            return Response(room_serializer.data)
        return Response(room_serializer.errors)

    elif request.method == 'DELETE':
        room = Room.objects.filter(id=pk).first()
        user.delete()
        return Response('deleted')
