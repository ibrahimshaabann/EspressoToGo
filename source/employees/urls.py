from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSetForAdmins, EmployeeLoginView, EmployeeSignUpView, CashierSignUpView

router = DefaultRouter()

router.register(r'^all-employees', EmployeeViewSetForAdmins, basename='employees')

urlpatterns = [
    path('', include(router.urls)),
    path('sign-up/', EmployeeSignUpView.as_view(), name='employee-sign-up'),
    path('login/', EmployeeLoginView.as_view(), name='employee-login'),
    path('cashier-sign-up/', CashierSignUpView.as_view(), name='cashier-sign-up'),

]
