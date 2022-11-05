from rest_framework.response import Response
from rest_framework.views import APIView
from apps.rooms.models import Room
from apps.rooms.api.serializers import RoomSerializer


class RoomApiView(APIView):

    def get(self, request):
        rooms = Room.objects.all()
        rooms_serializer = RoomSerializer(rooms, many=True)
        return Response(rooms_serializer.data)
