from django.contrib import admin
from .models import Category, Menu
from .filters import MenuFilter

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'available')
    list_filter = ( 'category', 'available')  

    search_fields = ('id','name', 'category__name')  

    def has_delete_permission(self, request, obj=None):
        return False  # Disables the Delete of the records


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    search_fields = ('name',)  # Add the search fields here
