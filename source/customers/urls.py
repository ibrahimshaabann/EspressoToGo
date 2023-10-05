from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AllCustomersViewSet, CustomerLoginView, CustomerSignUpView

router = DefaultRouter()

router.register(r'^all-customers', AllCustomersViewSet, basename='customers')

urlpatterns = [
    path('', include(router.urls)),
    path('sign-up/', CustomerSignUpView.as_view(), name='customer-sign-up'),
    # path('login/', CustomerLoginView.as_view(), name='customer-login'),
]
