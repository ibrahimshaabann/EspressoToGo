from rest_framework.routers import DefaultRouter
from .views import ShfitAdminViewSet, ShiftEmployeeViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'^employee/shift', ShiftEmployeeViewSet, basename='employee_shift')
router.register(r'^all_shifts', ShfitAdminViewSet, basename='all_shifts')
urlpatterns = [
    path('', include(router.urls))
]