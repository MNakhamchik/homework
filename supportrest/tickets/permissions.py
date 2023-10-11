from rest_framework import permissions


class IsSupportUserOrOwnerTicket(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'support':
            return True
        return obj.owner == request.user