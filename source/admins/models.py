from django.db import models

from users.models import Person


from .managers import AdminManager

import uuid

class AdminBridge(Person):
    """
    This is a proxy model for the Person model.
    It is used to create a separate table for the Admin model.
    This table will not be created on the postgres database tables.
    Instead, it will be used on the admins table as a 'bridge - connector - pointer' to the person model.
    """
    base_role = Person.Role.ADMIN

    class Meta:
        proxy = True

    objects = AdminManager()    # Custom Manager for the Admin model used only to filter the admins.




class Admin(AdminBridge):
    """
    This is the Admin model.
    It is used to create an Admin instance.
    """
    # admin_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    def save(self, force_update=True, commit=True, *args, **kwargs):
        
        self.is_staff = True
        self.is_superuser = True 
        
        if not self.role:
            self.role = self.base_role
        return super().save(force_update, commit, *args, **kwargs)


    class Meta:
        db_table = "admins"
        verbose_name = "Admin"
        verbose_name_plural = "الادمنز"
    

