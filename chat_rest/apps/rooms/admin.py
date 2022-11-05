from django.contrib import admin
from apps.rooms.models import Room


class RoomAdmin(admin.ModelAdmin):
    pass


admin.site.register(Room, RoomAdmin)
