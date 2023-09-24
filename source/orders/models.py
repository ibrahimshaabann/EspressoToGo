# from django.db import models

# from shifts.models import Shift


# class Order(models.Model):

#     ORDER_STATUS_CHOICES = [
#         ("PENDING", "Pending"),
#         ("CANCELED", "Canceled"),
#         ("DONE", "Done")
#     ]

#     ORDER_TYPE_CHOICES = [
#         ("HALL", "Hall"),
#         ("DELIVERY", "Delivery"),
#         ("OUTSIDE", "Outside"),
#     ]

#     order_status = models.CharField(max_length=12,
#                                     choices=ORDER_STATUS_CHOICES,
#                                     default="PENDING")
    
#     order_type = models.CharField(max_length=12,
#                                 choices=ORDER_TYPE_CHOICES,
#                                 default="HALL")
    
#     created_at = models.DateTimeField(null=False,
#                                       blank=False,
#                                       auto_now_add=True)
    
#     shift = models.ForeignKey(Shift,
#                             on_delete=models.SET_NULL,
#                             null=True,
#                             blank=True)
    

#     total_orice = models.DecimalField(null=False,
#                                       max_digits=9,
#                                       decimal_places=2,
#                                       default=0.00,
#                                       )

#     class Meta:
#         db_table = 'orders'
#         verbose_name = "Order"
#         verbose_name_plural = "orders"
#         ordering = ['-id']

#     def __str__(self) -> str:
#         return f"{self.id} {self.shift} {self.order_status}"
    
#     # customer = models.ForeignKey()


# class OrderItem(models.Model):

#     order = models.ForeignKey(Order, )

