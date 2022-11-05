from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('messages/', include('apps.chat_messages.urls')),
    path('rooms/', include('apps.rooms.urls')),
    path('admin/', admin.site.urls),
]
