from rest_framework import permissions


# Custom permission class
class IsSenderOrReceiver(permissions.BasePermission):
    """
    Permission check for is user sender or receiver
    """

    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user or obj.receiver == request.user

