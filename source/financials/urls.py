from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CostViewSet

router = DefaultRouter
router.register(r'costs', CostViewSet, basename='costs' )
urlpatterns=[
    path('', include(router.urls))
]