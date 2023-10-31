from django.contrib import admin
from .models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    list_display = ['customer','address']
    search_fields = ['customer__full_name','address','customer__phone_number']


# Register your models here.
