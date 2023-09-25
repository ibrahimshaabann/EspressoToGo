from collections.abc import Iterable
from django.db import models

from shifts.models import Shift

from products.models import Menu

from django.contrib.postgres.fields import ArrayField

class Order(models.Model):

    ORDER_STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("CANCELED", "Canceled"),
        ("DONE", "Done")
    ]

    ORDER_TYPE_CHOICES = [
        ("HALL", "Hall"),
        ("DELIVERY", "Delivery"),
        ("TAKEAWAY", "TakeAway"),
    ]

    order_status = models.CharField(max_length=12,
                                    choices=ORDER_STATUS_CHOICES,
                                    default="PENDING")
    
    order_type = models.CharField(max_length=12,
                                choices=ORDER_TYPE_CHOICES,
                                default="HALL")
    
    created_at = models.DateTimeField(null=False,
                                      blank=False,
                                      auto_now_add=True)
    
    shift = models.ForeignKey(Shift,
                            on_delete=models.SET_NULL,
                            null=True,
                            blank=True)
    

    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    
    # def update_total_price(self):
    #     total_price = 0.0
    #     for item in self.order_items.all(): 
    #         total_price += float(item.item_price) * int(item.quantity)

    #     return total_price


    class Meta:
        db_table = 'orders'
        verbose_name = "Order"
        verbose_name_plural = "orders"
        ordering = ['-id']

    def __str__(self) -> str:
        return f"{self.id} {self.shift} {self.order_status}"
    
    # customer = models.ForeignKey()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')

    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)
    
    item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    
    # def save(self, *args, **kwargs):
    #     self.item_price = self.menu_item.price
    #     self.total_price = self.item_price * self.quantity
        
    #     self.order.total_price = self.order.update_total_price()

    #     super(OrderItem, self).save(*args, **kwargs)
    #     self.order.save()




    class Meta:
        db_table = 'order_items'
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
        ordering = ['-id']