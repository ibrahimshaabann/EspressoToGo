from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSetForAdmins

router = DefaultRouter()

router.register(r'^all-employees', EmployeeViewSetForAdmins, basename='employees')

urlpatterns = [
    path('', include(router.urls)),
]
