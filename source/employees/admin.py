from django.contrib import admin

from .models import Employee

class EmployeeModelAdmin(admin.ModelAdmin):
    # readonly_fields = ("password",)
    exclude = ["last_login","groups","user_permissions","role","is_superuser","is_staff",]

    list_display= ("id","full_name", 'phone_number')
    

    # list_filter = ('full_name', 'phone_number',)  

    search_fields = ('full_name', 'phone_number')

    def has_delete_permission(self, request, obj=None):
        return False  # Disables the Delete of the records
    
    def save_model(self, request, obj, form, change):
        # Check if the password field has changed
        if change:
            original_obj = Employee.objects.get(pk=obj.pk)
            
            if original_obj.password != obj.password:
                obj.set_password(obj.password)
        else:
            # Creating a new object
            # Hash the password before saving the object
            obj.set_password(form.cleaned_data['password'])

        super().save_model(request, obj, form, change)



admin.site.register(Employee, EmployeeModelAdmin)
