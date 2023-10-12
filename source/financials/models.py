from django.db import models
from employees.models import Employee
from products.validators import validate_price

from users.models import Person

class Cost(models.Model):

    class Types (models.TextChoices):
        ADVANCE_PAYMENT = 'سلفه' 
        NORMAL_COST = 'تكلفه'

    description = models.CharField(verbose_name= 'الوصف',
                                   max_length=400,
                                   null=False,
                                   blank=False)
    price = models.DecimalField(max_digits=8,
                                decimal_places=2,
                                null=False,
                                blank=False,
                                validators=[validate_price],verbose_name="السعر")
    date = models.DateTimeField(verbose_name="وقت الدفع",
                                auto_now_add=True,null=True,blank=True)
    
    type = models.TextField(choices=Types.choices,
                            default=Types.NORMAL_COST,
                            blank=False,verbose_name="النوع")

    user = models.ForeignKey(Person,
                             verbose_name='مسئول الشيفت',
                             on_delete=models.SET_NULL,
                             null=True)
    related_shift = models.ForeignKey(
        "shifts.Shift",
        verbose_name='الشيفت المرتبط',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name = "Cost"
        verbose_name_plural = "المالية"
        db_table = "costs" 
        ordering = ['-id']


