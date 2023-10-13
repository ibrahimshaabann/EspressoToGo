from django.contrib import admin
from .models import Customer

# admin.site.register(Customer)
# 
class CustomerAdmin(admin.ModelAdmin):
    list_display= ("id","full_name", 'phone_number')
    

    # list_filter = ('full_name', 'phone_number',)  

    search_fields = ('full_name', 'phone_number')
    
    def has_delete_permission(self, request, obj=None):
        return False  # Disables the Delete of the records



admin.site.register(Customer,CustomerAdmin)