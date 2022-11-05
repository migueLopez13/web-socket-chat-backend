from django.urls import path
from apps.chat_messages.api.api import MessageApiView

urlpatterns = [
    path('', MessageApiView().as_view(), name='messages')
]
