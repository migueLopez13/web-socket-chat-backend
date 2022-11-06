from django.urls import path
from apps.rooms.api.api import room_api_view, room_detail_api_view

urlpatterns = [
    path('', room_api_view, name='rooms'),
    path('<int:pk>/', room_detail_api_view, name='room_detail')
]
