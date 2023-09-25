
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',include('products.urls')),
    path('financials/',include('financials.urls')),
    path('employees/', include('employees.urls')),
    path('admins/', include('admins.urls')),
    path('shifts/', include('shifts.urls')),
    path('orders/', include('orders.urls')),

]
