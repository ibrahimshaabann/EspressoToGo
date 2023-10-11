from django.contrib import admin
from .models import OrderItem
from .models import Order, OrderItem
# Register your models here.

class OrderItemsInline(admin.StackedInline):  #or admin.TabularInline
    model = OrderItem
    extra = 0 
@admin.register(Order)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_type', 'total_price_of_order','shift','customer')
    inlines = [OrderItemsInline]

@admin.register(OrderItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_item', 'quantity', 'item_price', 'total_price_of_order_items', 'order')

