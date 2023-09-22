from django.db import models

class Menu(models.Model):

    class Categories(models.TextChoices):
        PIZZA = 'pizza', 'Pizza'
        FOOD = 'food', 'Food'
        DRINKS = 'Drinks', 'drinks', 'drink', 'Drink'

    name = models.CharField(max_length=70,
                            null=False,
                            blank=False,
                            verbose_name="name")
    price = models.DecimalField(decimal_places=2,
                                max_digits=6,
                                null=False,
                                blank=False,
                                verbose_name="price")
    available = models.BooleanField(default=True,
                                    null=False,
                                    blank=False,
                                    verbose_name="is_available")
    category = models.TextField(choices=Categories.choices,
                                default=Categories.DRINKS,
                                null=False,
                                blank=False,
                                verbose_name="category")
    

    class Meta:
        db_table = "Menu"
        verbose_name = "Menu"
        verbose_name_plural = "Menu"


    def __str__(self) :
        return f"id: {self.id} Name:{self.name}"