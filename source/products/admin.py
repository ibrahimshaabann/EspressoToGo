from django.contrib import admin
from .models import Category, Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category','available')
    def has_delete_permission(self, request, obj=None):
        return False  # Disables the Delete of the records

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    

