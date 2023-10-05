from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AttendanceViewSet,AllAttendanceViewSet,EmployeeAttendanceViewSet

router = DefaultRouter()
router.register(r'in', AttendanceViewSet, basename='inattendance')
router.register(r'all', AllAttendanceViewSet, basename='allattendance')
router.register(r'employees', EmployeeAttendanceViewSet, basename='employees')

urlpatterns=[
    path('', include(router.urls))
]