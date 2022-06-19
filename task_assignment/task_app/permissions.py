"""
defining permission class to allow access to manager, employee
and clients respectively.
"""
from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    """give permission to manager users only."""

    def has_permission(self, request, view):
        is_not_client = (False if request.user.is_superuser else True)
        return bool(request.user and request.user.is_staff and is_not_client)


class IsEmployee(BasePermission):
    """give permission to employee users only."""

    def has_permission(self, request, view):
        is_not_client = (False if request.user.is_superuser else True)
        is_not_manager = (False if request.user.is_staff else True)
        return bool(request.user.is_authenticated and is_not_client and is_not_manager)


class IsClient(BasePermission):
    """give permission to client users only."""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
