from rest_framework.routers import DefaultRouter
from .views import ShfitReportViewSet, ShiftEmployeeViewSet, ShfitAdminViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'^employee/shift', ShiftEmployeeViewSet, basename='employee_shift')
router.register(r'^admin/all_shifts', ShfitAdminViewSet, basename="all_shifts")
router.register(r'^shift_reports', ShfitReportViewSet, basename='shift_reports')
urlpatterns = [
    path('', include(router.urls))
]