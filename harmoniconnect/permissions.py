from rest_framework.permissions import BasePermission

class IsServiceProvider(BasePermission):
    """Allows full access only to service providers and read-only access to others."""

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions are only allowed to the service provider or superuser.
        return request.user and request.user.is_authenticated and (
            request.user.is_superuser or request.user.is_service_provider
        )

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions are only allowed to the service provider of the service or superuser.
        # Assuming the Service model has a 'provider' field, and ServiceProvider has a 'user' field.
        if hasattr(obj, 'provider'):  # Checking if the object is a Service instance
            return obj.provider.user == request.user or request.user.is_superuser
        elif hasattr(obj, 'user'):  # Checking if the object is a ServiceProvider instance
            return obj.user == request.user or request.user.is_superuser
        return False
