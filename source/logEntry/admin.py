from django.contrib import admin

from .models import CustomLogEntry


class CustomLogEntryAdmin(admin.ModelAdmin):
    list_display = ( 'action_time', 'content_type', 'user', 'object_id', 'object_repr', 'action_flag', 'change_message')
    

admin.site.register(CustomLogEntry, CustomLogEntryAdmin)