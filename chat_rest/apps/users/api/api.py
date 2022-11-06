from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserWithRoomsSerializer


class UserApiView(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserWithRoomsSerializer(users, many=True)
        return Response(users_serializer.data)
