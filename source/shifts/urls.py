from rest_framework.routers import DefaultRouter
from .views import ShfitReportViewSet, ShfitViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'^all_shifts', ShfitViewSet, basename='all_shifts')
router.register(r'^shift_reports', ShfitReportViewSet, basename='shift_reports')
urlpatterns = [
    path('', include(router.urls))
]