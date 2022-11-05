from django.contrib import admin
from apps.users.models import User

admin.site.site_header = 'webChat'
admin.site.index_title = 'Administracion de chats'
admin.site.site_title = 'webChat'


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
