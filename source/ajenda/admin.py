from django.contrib import admin
from .models import Ajenda


@admin.register(Ajenda)
class AjendaAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_by', 'created', 'modified',)
    list_filter = ('created_by', 'created', 'modified')
    search_fields = ('description',)
    fields = ['description',]

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Check if it's a new instance
            obj.created_by = request.user
        obj.save()