from django.contrib import admin
from django.utils.html import format_html
from .models import Shift
from .views import ShfitAdminViewSet
from orders.models import Order

class ShiftInline(admin.StackedInline):  #or admin.TabularInline
    model = Order
    extra = 0 

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('id', 'responsible_employee', 'start_time', 'end_time', 'display_total_benefits', 'display_total_costs', 'display_net_profit')
    inlines = [ShiftInline]  # Add this line to display related OrderItem objects inline

    def has_change_permission(self, request, obj=None):
        return False  # Disables editing of the table

    def has_delete_permission(self, request, obj=None):
        return False  # Disables the Delete of the records
    
    def display_total_benefits(self, obj):
        benefits = obj.calculate_benefits()
        return benefits['total_benefits']

    display_total_benefits.short_description = 'اجمالي الشيفت'

    def display_total_costs(self, obj):
        benefits = obj.calculate_benefits()
        return benefits['total_costs']

    display_total_costs.short_description = 'المصاريف'

    def display_net_profit(self, obj):
        benefits = obj.calculate_benefits()
        return benefits['net_profit']

    display_net_profit.short_description = 'صافي الربح'
    
    readonly_fields = ('start_time','display_shift_menu_sales','display_total_benefits','display_total_costs', 'display_net_profit')

    def display_shift_menu_sales(self, obj):
        sales = obj.calc_menu_items_sales()
        return format_html('<br>'.join([f'{item["menu_item__name"]}: {item["quantity"]}' for item in sales]))

    display_shift_menu_sales.short_description = 'الاكثر مبيعاً' 
        
    def change_view(self, request, object_id, form_url='', extra_context=None):
        shift = Shift.objects.get(pk=object_id)
        benefits = shift.calculate_benefits()
        extra_context = extra_context or {}
        extra_context['benefits'] = benefits
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    change_view.short_description = "View Shift Benefits"

admin.site.register(Shift, ShiftAdmin)
