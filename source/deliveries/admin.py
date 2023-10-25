from django.contrib import admin

from .models import Delivery
@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    exclude = ("delivered",)
    list_display = ('id','description', 'address', 'for_order', 'responsible_employee',)
    list_filter = ('id','delivered', 'for_order', 'responsible_employee', 'created', 'modified')


    