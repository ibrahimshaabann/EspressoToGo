from django.contrib import admin

from .models import Employee

class EmployeeModelAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return True  # Disables the Delete of the records
    
    def save_model(self, request, obj, form, change):
        # Hash the password before saving the object
        obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)



admin.site.register(Employee, EmployeeModelAdmin)
