from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'pending-orders', views.PendingOrdersView, basename='pending-orders')

router.register(r'last-order', views.LastOrderView, basename='last-order')

router.register(r'^all', views.OrderViewSet, basename='orders')

router.register(r'^order-items', views.OrderItemsViewSet, basename='order-items')

router.register(r'^orders-admin', views.OrderViewSetAdmin, basename='order-admin')


urlpatterns = [
    path('', include(router.urls)),

    # path('pending-orders/', views.PendingOrdersView.as_view({'get': 'list'}), name='pending-orders'),

    # path('pending-orders/<int:pk>/', views.PendingOrdersView.as_view({'get': 'retrieve_order', 'patch': 'partial_update'}), name='pending-orders-detail'),


    # path('pending-orders/', views.PendingOrdersView.as_view(
    #     {
    #         'get' : 'list',
    #     }
    # ),
    # name='pending-orders'
    #      ),
         
    # path(
    #     'pending-orders/<int:pk>/', views.PendingOrdersView.as_view(
    #         {'patch':'partial_update'},
    #         name = 'pending-orders'
    #     )
    # )
]