from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)