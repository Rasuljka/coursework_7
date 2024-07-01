from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = 'Доступ запрещен'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
