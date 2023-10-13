
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('all', views.DeliveryViewSet, basename='all')

urlpatterns = [

    path('', include(router.urls)),
]
