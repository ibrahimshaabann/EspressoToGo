from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AttendanceViewSet,AllAttendanceViewSet

router = DefaultRouter()
router.register(r'in', AttendanceViewSet, basename='inattendance')
router.register(r'all', AllAttendanceViewSet, basename='allattendance')


urlpatterns=[
    path('', include(router.urls))
]