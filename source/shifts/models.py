from decimal import Decimal
from django.db import models
from employees.models import Employee
from financials.models import Cost
class Shift(models.Model):
    start_time = models.DateTimeField(null=False, #only null not blank 
                                      blank=True,
                                      verbose_name='وقت البداية',
                                      auto_now_add=True)
    end_time = models.DateTimeField(null=True,
                                    blank=True,
                                    verbose_name='وقت النهاية',
                                    # auto_now=True,
                                    default=None,
                                    ) ########################
    responsible_employee = models.ForeignKey(Employee, 
                                             null=True,
                                             on_delete=models.SET_NULL,)
    def calculate_benefits(self):
        from orders.models import Order
        total_order_price = Decimal(0)
        total_costs = Decimal(0)

        # Calculate total order price for orders within the shift's time frame
        orders_in_shift = Order.objects.filter(
            shift=self,
            created_at__gte=self.start_time,
            created_at__lte=self.end_time
        )

        for order in orders_in_shift:
            total_order_price += order.total_price_of_order

        # Calculate total costs for costs within the shift's time frame
        costs_in_shift = Cost.objects.filter(
            user=self.responsible_employee,
            date__gte=self.start_time,
            date__lte=self.end_time
        )

        for cost in costs_in_shift:
            total_costs += cost.price

        # Calculate benefits
        benefits = total_order_price - total_costs
        return {
            "total benefits": total_order_price,
            "total costs": total_costs,
            "net profit": benefits
        }
        # return f"Total Benefits: {total_order_price} // Total Costs: {total_costs} // Net Profits: {benefits}"
    

    class Meta:
        db_table = 'shifts'
        verbose_name = 'Shift'
        verbose_name_plural = 'shifts'
        ordering = ['-id']

    def __str__(self) :
        return f"Responsible Emoloyee: {self.responsible_employee.full_name}"

    


class ShiftReport(models.Model):
    # sum total of orders in the shift object related to the shift report
    total_profit = models.DecimalField(null=True,
                                       blank=True,
                                       decimal_places=2,
                                       max_digits=9,
                                       verbose_name='اجمالي الربح')
    
    # sum of cost in shift object of shift report
    total_costs = models.DecimalField(null=True,
                                      blank=True,
                                      decimal_places=2,
                                      max_digits=9,
                                      verbose_name='اجمالي التكلفة')

    # net_profit = total_profit - total_costs
    net_profit = models.DecimalField(null=True,
                                    blank=True,
                                    decimal_places=2,
                                    max_digits=9,
                                    verbose_name='صافي الربح')
    
    # Each shift report has one shift nad shift has one shift report
    related_shift = models.OneToOneField(Shift,
                                        null=False,
                                        blank=False,
                                        on_delete=models.PROTECT,
                                        verbose_name='الشيفت',
                                        related_name="shifts")
    


    # time_duration = models.DurationField(null=True, blank=True, verbose_name='مدة الشيفت')

    


    class Meta:
        db_table = 'shifts_reports'
        verbose_name = 'Shift Report'
        verbose_name_plural = 'Shifts Reports'
        ordering = ['-id']

    def __str__(self) -> str:
        return f"related shift: {self.related_shift.responsible_employee.full_name}"
    
    