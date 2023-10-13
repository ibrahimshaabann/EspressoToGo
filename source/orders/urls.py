from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'last-order', views.PendingOrderView, basename='last-order')

router.register(r'^all', views.OrderViewSet, basename='orders')

router.register(r'^order-items', views.OrderItemsViewSet, basename='order-items')

router.register(r'^orders-admin', views.OrderViewSetAdmin, basename='order-items')


urlpatterns = [
    path('', include(router.urls)),
]