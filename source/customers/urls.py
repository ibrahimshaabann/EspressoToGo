from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomerViewSetForAdmins, CustomerLoginView, CustomerSignUpView

router = DefaultRouter()

router.register(r'^all-customers', CustomerViewSetForAdmins, basename='customers')

urlpatterns = [
    path('', include(router.urls)),
    path('sign-up/', CustomerSignUpView.as_view(), name='customer-sign-up'),
    path('login/', CustomerLoginView.as_view(), name='customer-login'),
]
