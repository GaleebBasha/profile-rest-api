from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        print("method nmae is", request.method)
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.id
