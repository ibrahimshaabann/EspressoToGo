from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'^all', views.OrderViewSet, basename='orders')

router.register(r'^order-items', views.OrderItemsViewSet, basename='order-items')


urlpatterns = [
    path('', include(router.urls)),
]