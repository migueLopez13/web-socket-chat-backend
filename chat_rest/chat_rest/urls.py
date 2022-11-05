from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('users/', include('apps.users.api.urls')),
        path('messages/', include('apps.chat_messages.api.urls')),
        path('rooms/', include('apps.rooms.api.urls')),
    ])
    ),
]
