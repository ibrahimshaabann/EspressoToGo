from admincharts.admin import AdminChartMixin
from .models import Menu
class MenuPriceChart(AdminChartMixin):
    title = 'Menu Prices'
    model = Menu
    group_by = 'category__name'
    aggregate = 'Avg'
    aggregate_field = 'price'
    chart_type = 'bar'