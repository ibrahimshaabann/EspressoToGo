from django.contrib import admin
from .models import Shift, ShiftReport


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time', 'responsible_employee')


@admin.register(ShiftReport)
class ShiftReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_profit', 'total_costs', 'net_profit', 'related_shift')



