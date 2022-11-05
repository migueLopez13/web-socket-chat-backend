from django.urls import path
from apps.rooms.api.api import RoomApiView

urlpatterns = [
    path('', RoomApiView().as_view(), name='rooms')
]
