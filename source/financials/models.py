from django.db import models
from products.validators import validate_price

class Cost(models.Model):
    description = models.CharField(verbose_name= 'الوصف',
                                   max_length=400,
                                   null=False,
                                   blank=False)
    price = models.DecimalField(max_digits=8,
                                decimal_places=2,
                                null=False,
                                blank=False,
                                validators=[validate_price])
    date = models.DateTimeField(verbose_name="وقت الدفع",
                                auto_now_add=True)
    
    # user = models.ForeignKey(Person, verbose_name='مسئول الشيفت', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Cost"
        verbose_name_plural = "Costs"
        db_table = "costs" 
        ordering = ['-id']
