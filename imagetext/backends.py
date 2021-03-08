"""Backend for access"""
from django.contrib.auth.backends import RemoteUserBackend
from django.core.exceptions import PermissionDenied


class ImagetextUserBackend(RemoteUserBackend):
    """Authenticate user, else deny permission."""

    def authenticate(self, request, remote_user):
        """Authenticate user into Imagetext."""
        if not remote_user:
            raise PermissionDenied()
