from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from vocgui.models import TrainingSet
from vocgui.serializers import GroupSerializer
from vocgui.permissions import VerifyGroupKey
from vocgui.models import GroupAPIKey
from vocgui.utils import get_key


class GroupViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    Defines a view set for the Group module.
    Inherits from `viewsets.ModelViewSet` and defines queryset
    and serializers.
    """

    permission_classes = [VerifyGroupKey]
    serializer_class = GroupSerializer
    http_method_names = ["get"]

    def get_queryset(self):
        """
        Defining custom queryset

        :raises PermissionDenied: Exception if invalid API-Key is delivered
        :return: (filtered) queryset
        :rtype: QuerySet
        """
        if getattr(self, "swagger_fake_view", False):
            return TrainingSet.objects.none()
        key = get_key(self.request)
        if not key:
            raise PermissionDenied()
        try:
            api_key_object = GroupAPIKey.objects.get_from_key(key)
        except GroupAPIKey.DoesNotExist as e:
            raise PermissionDenied() from e
        if not api_key_object:
            raise PermissionDenied()
        queryset = Group.objects.filter(id=api_key_object.organization_id)
        return queryset
