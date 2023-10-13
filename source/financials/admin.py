from django.contrib import admin
from .models import Cost
from .views import BenefitsViewSet
from decimal import Decimal
from orders.models import Order
from django.urls import path
from django.shortcuts import render
@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ['description', 'price', 'date' , 'type','user']

# @admin.site.admin_view
# def benefits_admin_view(request):
#     if request.method == 'POST':
#         start_date = request.POST.get('start_date')
#         end_date = request.POST.get('end_date')

#         total_orders_prices = Decimal(0)
#         total_costs = Decimal(0)    
#         orders_in_duration = Order.objects.filter(
#             created_at__gte=start_date,
#             created_at__lte=end_date
#         )
#         for order in orders_in_duration:
#             total_orders_prices += order.total_price_of_order

#         costs_in_duration = Cost.objects.filter(
#             related_shift__start_time__gte=start_date,
#             related_shift__end_time__lte=end_date
#         )

#         for cost in costs_in_duration:
#             total_costs += cost.price
#         net_profit = total_orders_prices - total_costs

#         context = {
#             'start_date': start_date,
#             'end_date': end_date,
#             'total_orders_prices': total_orders_prices,
#             'total_costs': total_costs,
#             'net_profit': net_profit
#         }
#         # Use Jazzmin's admin templates for rendering
#         return render(request, 'financials/benefits_admin.html', context)
#     else:
#         return render(request, 'financials/benefits_admin.html')