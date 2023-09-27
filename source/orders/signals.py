from django.db.models.signals import (
    pre_save, post_save, pre_delete, post_delete
)
from django.dispatch import receiver

from .models import *


@receiver(pre_save, sender=OrderItem)
def set_item_price_of_order_item(sender, instance, **kwargs):
    instance.item_price = instance.menu_item.price



# @receiver(post_save, sender=Order)
# def update_total_price_of_order(sender, instance, **kwargs):
#     order_items = OrderItem.objects.filter(order=instance)
#     total_price = sum(item.total_price_of_order_items for item in order_items)
#     if instance.total_price < total_price:
#         raise Exception("Total price of order is less than total price of order items")


@receiver(pre_save, sender=OrderItem)
def update_total_price_of_order_item(sender, instance, **kwargs):
    instance.total_price_of_order_items = instance.menu_item.price * instance.quantity


@receiver(post_save, sender=OrderItem)
def update_total_price_of_order(sender, instance, **kwargs):
    order = instance.order
    order_items = order.order_items.all()
    total_price = sum(item.total_price_of_order_items for item in order_items)
    order.total_price = total_price
    order.save()



@receiver(post_delete, sender=OrderItem)
def update_total_price_on_delete(sender, instance, **kwargs):
    order = instance.order
    order_items = order.order_items.all()
    total_price = sum(item.total_price_of_order_items for item in order_items)
    order.total_price = total_price
    order.save()