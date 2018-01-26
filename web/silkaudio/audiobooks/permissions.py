from rest_framework import permissions


class HasReadOrStaffPermission(permissions.BasePermission):
    def has_read_or_staff_permission(self, request):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # # Write permissions are only allowed to the owner of the snippet.
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return self.has_read_or_staff_permission(request)

    def has_permission(self, request, view):
        return self.has_read_or_staff_permission(request)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user
