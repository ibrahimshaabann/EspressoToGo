from django.urls import path, include
from rest_framework import routers

from . import views

# router = routers.DefaultRouter()


urlpatterns = [
    # path('', include(router.urls), name='admins'),
    path('sign-up/', views.AdminSignUpView.as_view(), name='admin-sign-up'),
    path('login/', views.AdminLoginView.as_view(), name='admin-login'),
    path('all-admins/', views.AllAdminsViewSet.as_view(), name='all-admins'),

]
