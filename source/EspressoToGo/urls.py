
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings


schema_view = get_schema_view(
    openapi.Info(
        title="Swagger API",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

admin.site.index_template = "admin/index.html"

urlpatterns = [
    # path('admin/', admin.site.urls),

    # For Production
    path('0mysecureadminpanelurl1/', admin.site.urls),
    path('products/',include('products.urls')),
    path('financials/',include('financials.urls')),
    path('employees/', include('employees.urls')),
    path('attendance/', include('attendance.urls')),
    path('admins/', include('admins.urls')),
    path('shifts/', include('shifts.urls')),
    path('orders/', include('orders.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('deliveries/', include('deliveries.urls')),
    path('customers/', include('customers.urls')),
    path('ajenda/', include('ajenda.urls')),
    path('address/', include('address.urls')),

]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.views.static import serve
urlpatterns += [ re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]