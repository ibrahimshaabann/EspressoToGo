from django.db import models, transaction

from shifts.models import Shift

from products.models import Menu

from customers.models import Customer


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



    class Meta:
        db_table = 'orders'
        verbose_name = "Order"
        verbose_name_plural = "orders"
        ordering = ['-id']

        # unique_together = ('', '')

    def __str__(self) -> str:
        return f"Order: {self.id}.\t Status: {self.order_status}"
    
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')

    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)
    
    item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    
    total_price_of_order_items = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True) 


    class Meta:
        db_table = 'order_items'
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
        ordering = ['-id']


    def __str__(self):
        return f"{self.menu_item.name}: {self.quantity}"