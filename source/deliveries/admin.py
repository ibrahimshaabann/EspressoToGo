from django.contrib import admin

from .models import Delivery
@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('description', 'address', 'delivered', 'for_order', 'responsible_employee', 'created', 'modified')
    list_filter = ('delivered', 'for_order', 'responsible_employee', 'created', 'modified')