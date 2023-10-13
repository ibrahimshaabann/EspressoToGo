from django.contrib import admin
from .models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = (  "employee_attended" ,"in_time" ,"out_time" ,"user_created_the_attendance")
    fields = ["employee_attended"  ,"out_time" ,"user_created_the_attendance",]
    list_filter = ["employee_attended__full_name","in_time","out_time"]
    search_fields = ["employee_attended__full_name","employee_attended__phone_number",]
admin.site.register(Attendance,AttendanceAdmin)
# Register your models here.
