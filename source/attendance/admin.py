from django.contrib import admin
from .models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = (  "employee_attended" ,"in_time" ,"out_time" ,"user_created_the_attendance")

admin.site.register(Attendance,AttendanceAdmin)
# Register your models here.
