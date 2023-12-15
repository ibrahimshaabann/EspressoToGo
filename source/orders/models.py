from django.db import models, transaction

from shifts.models import Shift

from products.models import Menu
from products.validators import validate_price
from customers.models import Customer
from address.models import Address


class Order(models.Model):

    ORDER_STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("CANCELED", "Canceled"), ## what happens if the order got cancelled as benefits ? 
        ("DONE", "Done")
    ]

    ORDER_TYPE_CHOICES = [
        ("HALL", "Hall"),
        ("DELIVERY", "Delivery"),
        ("TAKEAWAY", "TakeAway"),
    ]

    order_status = models.CharField(max_length=12,
                                    choices=ORDER_STATUS_CHOICES,
                                    default="PENDING",verbose_name="حالة الاوردر")
    
    order_type = models.CharField(max_length=12,
                                choices=ORDER_TYPE_CHOICES,
                                default="HALL",verbose_name="نوع الاوردر")
    
    created_at = models.DateTimeField(null=False,
                                      blank=False,
                                      auto_now_add=True,verbose_name="وقت الاودر")
    
    shift = models.ForeignKey(Shift,
                            on_delete=models.PROTECT,
                            null=False,
                            blank=False,
                            related_name='orders',verbose_name="الشيفت")
    
    total_price_of_order = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True,verbose_name="اجمالي السعر")
    tax = models.DecimalField(blank=True, null=True,  verbose_name="سعر التوصيل", max_digits=7, decimal_places=2, validators=[validate_price])
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null = True, blank=True,verbose_name="العنوان ")
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='orders', null=True, blank=True,verbose_name="العميل")

    # An alternative for order_id, this attribute is created to start from 1 with each new shift
    order_number = models.IntegerField(null=False, blank=False, verbose_name='رقم الأوردر', default=0, db_index=True)

    class Meta:
        db_table = 'orders'
        verbose_name = "Order"
        verbose_name_plural = "الاوردرات"
        ordering = ['-id']
    
    def __str__(self) -> str:
        return f"{self.pk}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items',verbose_name="الاوردر")

    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_item',verbose_name="الاسم")

    quantity = models.PositiveIntegerField(default=1,verbose_name="الكمية")
    
    item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True,verbose_name="سعر العنصر")
    
    total_price_of_order_items = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True,verbose_name="اجمالي العناصر")
    
    class Meta:
        db_table = 'order_items'
        verbose_name = "Order Item"
        verbose_name_plural = "عناصر الاوردر"
        ordering = ['-id']


    def __str__(self):
        return f"{self.menu_item.name}: {self.quantity}"