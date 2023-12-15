from django.db.models.signals import (pre_save, post_save, pre_delete, post_delete)
from django.dispatch import receiver
from .models import *


@receiver(pre_save, sender=OrderItem)
def set_item_price_of_order_item(sender, instance, **kwargs):
    """used
    This signal is  to set the item price of order item when an order item is created or updated
    """

    instance.item_price = instance.menu_item.price


@receiver(pre_save, sender=OrderItem)
def update_total_price_of_order_item(sender, instance, **kwargs):
    """
    This signal is used to update the total price of order item when an order item is created or updated
    """
    instance.total_price_of_order_items = instance.menu_item.price * instance.quantity


@receiver(post_save, sender=OrderItem)
def update_total_price_of_order(sender, instance, **kwargs):
    """
    This signal is used to update the total price of order when an order item is created or updated
    """
    order = instance.order
    order_items = order.order_items.all()
    total_price = sum(item.total_price_of_order_items for item in order_items)
    order.total_price_of_order = total_price
    order.save()

@receiver(post_delete, sender=OrderItem)
def update_total_price_on_delete(sender, instance, **kwargs):
    """
    This signal is used to update the total price of order when an order item is deleted
    """
    order = instance.order
    order_items = order.order_items.all()
    total_price = sum(item.total_price_of_order_items for item in order_items)
    order.total_price_of_order = total_price
    order.save()



