from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AttendanceViewSet

router = DefaultRouter()
router.register(r'', AttendanceViewSet, basename='attendance')

urlpatterns=[
    path('', include(router.urls))
]