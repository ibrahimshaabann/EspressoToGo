from decimal import Decimal
from django.db import models
from employees.models import Employee
from financials.models import Cost
from django.db.models import Sum

class Shift(models.Model):
    start_time = models.DateTimeField(null=False, #only null not blank 
                                      blank=True,
                                      verbose_name='وقت البداية',
                                      auto_now_add=True,
                                      )
    end_time = models.DateTimeField(null=True,
                                    blank=True,
                                    verbose_name='وقت النهاية',
                                    # auto_now=True,
                                    default=None,
                                    )
    responsible_employee = models.ForeignKey(Employee, 
                                             null=True,
                                             on_delete=models.SET_NULL,verbose_name="مسئول الشيفت")
    
    def calculate_benefits(self):
        from orders.models import Order
        total_order_price = Decimal(0)
        total_costs = Decimal(0)

        # Calculate total order price for orders within the shift
        orders_in_shift = Order.objects.filter(shift_id=self.id)

        for order in orders_in_shift:
            total_order_price += order.total_price_of_order

        # Calculate total costs for costs within the shift
        costs_in_shift = Cost.objects.filter(related_shift_id=self.id)

        for cost in costs_in_shift:
            total_costs += cost.price

        # Calculate benefits
        benefits = total_order_price - total_costs
        return {
            "total_benefits": total_order_price,
            "total_costs": total_costs,
            "net_profit": benefits
        }
    

    """
    you can use the next query to provide staes fot the admin dashboard:
        - Most menu items sales
        - least menu items sales
        - total customers
        - Top categories
        - Down categories
        - Top menu item sales
        - Down menu item sales
    """
    
    def calc_menu_items_sales(self):
        from orders .models import OrderItem
        search_shift = self

        menu_sales_in_shift = list(  # here we cast the queryset to list
            OrderItem.objects.filter( 
                order__shift = search_shift #getting all order items related to the search shift
            ).values(
               'menu_item__name' 
            ).annotate(
                quantity = Sum('quantity') 
            ).order_by(
                '-quantity'
            )
        )

        return  menu_sales_in_shift


    class Meta:
        db_table = 'shifts'
        verbose_name = 'Shift'
        verbose_name_plural = 'الشيفتات'
        ordering = ['-id']

    def __str__(self) :
        print(self.responsible_employee)
        return f"Responsible Emoloyee: {self.responsible_employee.full_name}"

    
# class ShiftReport(models.Model):
#     # sum total of orders in the shift object related to the shift report
#     total_profit = models.DecimalField(null=True,
#                                        blank=True,
#                                        decimal_places=2,
#                                        max_digits=9,
#                                        verbose_name='اجمالي الربح')
    
#     # sum of cost in shift object of shift report
#     total_costs = models.DecimalField(null=True,
#                                       blank=True,
#                                       decimal_places=2,
#                                       max_digits=9,
#                                       verbose_name='اجمالي التكلفة')

#     # net_profit = total_profit - total_costs
#     net_profit = models.DecimalField(null=True,
#                                     blank=True,
#                                     decimal_places=2,
#                                     max_digits=9,
#                                     verbose_name='صافي الربح')
    
#     # Each shift report has one shift nad shift has one shift report
#     related_shift = models.OneToOneField(Shift,
#                                         null=False,
#                                         blank=False,
#                                         on_delete=models.PROTECT,
#                                         verbose_name='الشيفت',
#                                         related_name="shifts")
    


#     # time_duration = models.DurationField(null=True, blank=True, verbose_name='مدة الشيفت')



#     class Meta:
#         db_table = 'shifts_reports'
#         verbose_name = 'Shift Report'
#         verbose_name_plural = 'تقارير الشيفتات'
#         ordering = ['-id']

#     def __str__(self) -> str:
#         return f"related shift: {self.related_shift.responsible_employee.full_name}"
    
    