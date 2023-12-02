from django.contrib import admin
from .models import OrderItem
from .models import Order, OrderItem
# Register your models here.

class OrderItemsInline(admin.StackedInline):  #or admin.TabularInline
    model = OrderItem
    extra = 0 
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_type', 'total_price_of_order','shift','customer', 'created_at', 'order_number')
    inlines = [OrderItemsInline]
    list_filter = ["created_at","order_status","customer","order_type"]
    search_fields = ["id",]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_item', 'quantity', 'item_price', 'total_price_of_order_items', 'order')
    list_filter = ["menu_item",]
    search_fields = ["order__id","menu_item__name",]
