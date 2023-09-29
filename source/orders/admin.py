from django.contrib import admin

# Register your models here.

from .models import Order, OrderItem
@admin.register(Order)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_type', 'total_price_of_order','shift','customer')


@admin.register(OrderItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_item', 'quantity', 'item_price', 'total_price_of_order_items', 'order')

