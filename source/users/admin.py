from django.contrib import admin
from django.contrib.auth.models import Group
from django.http.request import HttpRequest
from .models import Person


class PersonModelAdmin(admin.ModelAdmin):
    # list_editable = ["password",]
    # readonly_fields = ["password",]
    exclude = ["last_login","groups","user_permissions","role","is_superuser","is_staff",]
    list_display = ["full_name"]
    def has_delete_permission(self, request, obj=None):
        return False  # Disables the Delete of the records
    
    
    def save_model(self, request, obj, form, change):
        # Check if the password field has changed
        if change:
            original_obj = Person.objects.get(pk=obj.pk)
            
            if original_obj.password != obj.password:
                obj.set_password(obj.password)
        else:
            # Creating a new object
            # Hash the password before saving the object
            obj.set_password(form.cleaned_data['password'])

        super().save_model(request, obj, form, change)


admin.site.register(Person, PersonModelAdmin)
admin.site.unregister(Group)