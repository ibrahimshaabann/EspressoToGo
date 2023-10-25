from collections.abc import Iterable
from django.db import models
from models_extensions.models import TimeStampedModel
from users.models import Person


class Ajenda(TimeStampedModel):
    description = models.TextField(verbose_name="ملاحظه", blank=False, null=False)
    created_by = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="المسئول")

    class Meta:
        db_table = "ajenda"
        verbose_name = "ملحوظة"
        verbose_name_plural = "ملاحظات"