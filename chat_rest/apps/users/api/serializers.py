from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'user_permissions', 'groups']


class UserWithRoomsSerializer(serializers.ModelSerializer):
    rooms = serializers.SerializerMethodField()

    def get_rooms(self, instance):
        from apps.rooms.api.serializers import RoomRelationSerializer
        return RoomRelationSerializer(instance.rooms, many=True).data

    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'user_permissions', 'groups']


class UserOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'avatar']


class UserRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'name',
            'surname',
            'avatar',
            'created_at',
            'updated_at'
        ]
