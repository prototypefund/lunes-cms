from django.core.exceptions import PermissionDenied
from rest_framework import permissions
from .models import GroupAPIKey
from .utils import get_key


class VerifyGroupKey(permissions.AllowAny):
    """Simple permissions class that blocks
    requests if no valid API-Token is delivered.
    Inherits from `permissions.AllowAny`.
    """

    def has_permission(self, request, view):
        """Checks whether a valid API-Key is send
        by the user in the authorization header

        :param request: http request
        :type request: HttpRequest
        :param view: restframework view
        :type view: viewsets.ModelViewSet
        :raises PermissionDenied: Exception if invalid API-Key is delivered
        :return: False if user doesn't send a API-key
        :rtype: bool
        """
        key = get_key(request)
        if key is None:
            return False
        try:
            _ = GroupAPIKey.objects.get_from_key(key)
        except GroupAPIKey.DoesNotExist as e:
            raise PermissionDenied() from e
        return True
