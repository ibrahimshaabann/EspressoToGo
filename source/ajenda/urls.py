from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import AjendaViewSet


router = DefaultRouter()
router.register(r'^ajenda', AjendaViewSet, basename='ajenda')

urlpatterns = [
    path('', include(router.urls))
]