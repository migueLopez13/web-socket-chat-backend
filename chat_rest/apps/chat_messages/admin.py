from django.contrib import admin
from apps.chat_messages.models import Message


class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Message, MessageAdmin)
