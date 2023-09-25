from django.contrib import admin

# Register your models here.

from .models import Shift, ShiftReport

admin.site.register(Shift)
admin.site.register(ShiftReport)
