from django.db import models

from django.contrib.admin.models import LogEntry


class CustomLogEntry(LogEntry):
    class Meta:
        verbose_name = "اخر حدث"
        verbose_name_plural = "الاحداث الاخيرة"
        proxy = True