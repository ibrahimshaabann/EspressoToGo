from django.db import models
from employees.models import Employee

class Shift(models.Model):
    start_time = models.DateTimeField(null=False, #only null not blank 
                                      blank=True,
                                      verbose_name='وقت البداية',
                                      auto_now_add=True)
    end_time = models.DateTimeField(null=True,
                                    blank=True,
                                    verbose_name='وقت النهاية',
                                    auto_now=True) ########################
    responsible_employee = models.ForeignKey(Employee, 
                                             null=True,
                                             on_delete=models.SET_NULL,)
    
    class Meta:
        db_table = 'shifts'
        verbose_name = 'Shift'
        verbose_name_plural = 'shifts'
        ordering = ['-id']

    def __str__(self) :
        return f"Responsible Emoloyee: {self.responsible_employee.full_name}"

    


class ShiftReport(models.Model):
    # sum total of orders in the shift object related to the shift report
    total_profit = models.DecimalField(null=False,
                                       blank=False,
                                       decimal_places=2,
                                       max_digits=9,
                                       verbose_name='اجمالي الربح')
    
    # sum of cost in shift object of shift report
    total_costs = models.DecimalField(null=False,
                                      blank=False,
                                      decimal_places=2,
                                      max_digits=9,
                                      verbose_name='')

    # net_profit = total_profit - total_costs
    net_profit = models.DecimalField(null=False,
                                    blank=False,
                                    decimal_places=2,
                                    max_digits=9,
                                    verbose_name='صافي الربح')
    
    # Each shift report has one shift nad shift has one shift report
    related_shift = models.OneToOneField(Shift,
                                        null=False,
                                        blank=False,
                                        on_delete=models.PROTECT,
                                        verbose_name='الشيفت')
    
    class Meta:
        db_table = 'shifts_reports'
        verbose_name = 'Shift Report'
        verbose_name_plural = 'Shifts Reports'
        ordering = ['-id']

    def __str__(self) -> str:
        return f"related shift: {self.related_shift.responsible_employee.full_name}"
    
    