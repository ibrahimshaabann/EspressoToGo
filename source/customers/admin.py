from django.contrib import admin
from .models import Customer

# admin.site.register(Customer)
# 
class CustomerAdmin(admin.ModelAdmin):
    list_display= ("id","full_name",)
    def has_delete_permission(self, request, obj=None):
        return False  # Disables the Delete of the records



admin.site.register(Customer,CustomerAdmin)