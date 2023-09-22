from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MenuViewSet

router = DefaultRouter()
router.register(r'menu', MenuViewSet, basename='api/menu/')
urlpatterns= [
    path('', include(router.urls)),
]