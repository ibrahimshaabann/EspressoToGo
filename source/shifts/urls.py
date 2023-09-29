from rest_framework.routers import DefaultRouter
from .views import ShfitReportViewSet, ShfitAdminViewSet, ShiftEmployeeViewSet, ShfitBenefitsViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'^all_shifts', ShfitAdminViewSet, basename='all_shifts')
router.register(r'^shift_reports', ShfitBenefitsViewSet, basename='shift_reports')
urlpatterns = [
    path('', include(router.urls))
]