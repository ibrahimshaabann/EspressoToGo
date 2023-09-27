from django.db import models
from .validators import validate_price
    

class Category(models.Model):
    name = models.CharField(null=False, 
                            blank=False,
                            max_length=95,
                            verbose_name="category name")
    

    class Meta:
        verbose_name = "Catrgory"
        verbose_name_plural = "Categories"
        db_table = "categories"
        ordering = ['name']


    def __str__(self) -> str:
        return f"{self.name}"
    
   
class Menu(models.Model):

    name = models.CharField(max_length=70,
                            null=False,
                            blank=False,
                            verbose_name="name")
    price = models.DecimalField(decimal_places=2,
                                max_digits=6,
                                null=False,
                                blank=False,
                                verbose_name="price",
                                validators=[validate_price])
    available = models.BooleanField(default=True,
                                    null=False,
                                    blank=False,
                                    verbose_name="is_available")
    
    category = models.ForeignKey(Category,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name="category"   
                                )

    class Meta:
        db_table = "menu_items"
        verbose_name = "Menu"
        verbose_name_plural = "menu_items"
        ordering = ['-id'] # descending order


    def __str__(self):
        return self.name