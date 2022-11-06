from django.urls import path
from apps.chat_messages.api.api import message_api_view, message_detail_api_view

urlpatterns = [
    path('', message_api_view, name='messages'),
    path('<int:pk>/', message_detail_api_view, name='message_detail')
]
