from rest_framework import permissions

class IsAccountHolder(permissions.BasePermission):
    
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False