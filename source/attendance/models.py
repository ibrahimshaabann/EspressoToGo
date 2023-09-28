from django.db import models
from users.models import Person
from employees.models import Employee


class Attendance(models.Model):
    employee_attended = models.ForeignKey(Employee,related_name="employee_attendance", on_delete=models.CASCADE,null=True, verbose_name='الموظف',)
    in_time = models.DateTimeField(auto_now_add=True,verbose_name='وقت الدخول', null=True, blank=True)
    out_time = models.DateTimeField(verbose_name='وقت الخروج', null=True, blank=True)
    user_created_the_attendance =  models.ForeignKey(Person,related_name="user_created", on_delete=models.SET_NULL,null=True,verbose_name= "المسئول")
    
    class Meta:
        verbose_name_plural = "الحضور والانصراف"
        db_table = "Attendance"
        ordering = ["-in_time"]
    def __str__(self):
        return f"{self.employee_attended.full_name}"
