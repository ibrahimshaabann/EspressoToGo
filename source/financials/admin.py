from django.contrib import admin
from .models import Cost
@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ['description', 'price', 'date' , 'type','user']
    list_filter = ['date','user','type',]
    search_fields = ['user__full_name','description',]