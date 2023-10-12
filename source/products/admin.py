from django.contrib import admin
from .models import Category, Menu
from admincharts.admin import AdminChartMixin
from .charts import MenuPriceChart

@admin.register(Menu)
class MenuAdmin(AdminChartMixin,admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category','available')
    chart_list = [MenuPriceChart]
    def has_delete_permission(self, request, obj=None):
        return False  # Disables the Delete of the records

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    

