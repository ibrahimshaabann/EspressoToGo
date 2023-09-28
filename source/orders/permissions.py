from rest_framework.permissions import BasePermission, SAFE_METHODS


class _(BasePermission):
    def has_permission(self, request, view):
        pass
    def has_object_permission(self, request, view, obj):
        pass