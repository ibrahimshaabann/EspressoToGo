from django.contrib import admin

from .models import Delivery
@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'delivered', 'for_order', 'reposnisble_employee', 'created', 'modified')
    list_filter = ('delivered', 'for_order', 'reposnisble_employee', 'created', 'modified')