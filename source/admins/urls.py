from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls), name='admins'),
    path('login/', views.AdminLoginView.as_view(), name='admin-login'),
]
