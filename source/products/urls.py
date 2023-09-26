from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MenuViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'^menu', MenuViewSet, basename='menu/')
router.register(r'^categories', CategoryViewSet, basename='categories/')

urlpatterns= [
    path('', include(router.urls)),
]