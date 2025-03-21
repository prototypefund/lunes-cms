from django.db.models import Count, Q
from django.core.exceptions import PermissionDenied
from vocgui.models import Discipline
from vocgui.utils import get_child_count, get_key
from vocgui.models import GroupAPIKey


def get_filtered_discipline_queryset(discipline_view_set):
    """Returns child disciplines belonging to the discipline id
    of the passed discipline view set. Only released and non-empty
    objects are returned. The number of training sets contained by
    a child is annotated as well.

    :param discipline_view_set: A handle to the :class:`DisciplineViewSet`
    :type discipline_view_set: class
    :return: (filtered) queryset
    :rtype: QuerySet
    """
    queryset = Discipline.objects.filter(
        Q(released=True)
        & Q(
            id__in=Discipline.objects.get(
                id=discipline_view_set.kwargs["discipline_id"]
            ).get_children()
        )
    ).annotate(
        total_training_sets=Count(
            "training_sets", filter=Q(training_sets__released=True)
        ),
    )
    queryset = get_non_empty_disciplines(queryset)
    return queryset


def get_overview_discipline_queryset():
    """Returns the general disciplines created by super users if the are
    root nodes and recursively either has at least one sub-discipline or one
    training set. Additionally, they need to be released by the creator group.

    :return: (filtered) queryset
    :rtype: QuerySet
    """
    queryset = Discipline.objects.filter(
        Q(released=True) & Q(creator_is_admin=True)
    ).annotate(
        total_training_sets=Count(
            "training_sets", filter=Q(training_sets__released=True)
        ),
    )
    queryset = [obj for obj in queryset if obj.is_root_node()]
    queryset = get_non_empty_disciplines(queryset)
    return queryset


def get_discipline_by_group_queryset(discipline_view_set):
    """Returns overview of disciplines for a given group id, which must be
    in the keyword arguments of the passed discipline view set. All elements are
    root nodes and recursively either have at least one sub-discipline or one
    training set. Additionally, they need to be released by the creator group.

    :param discipline_view_set: A handle to the :class:`DisciplineViewSet`
    :type discipline_view_set: class
    :return: (filtered) queryset
    :rtype: QuerySet
    """
    queryset = Discipline.objects.filter(
        released=True, created_by=discipline_view_set.kwargs["group_id"]
    ).annotate(
        total_training_sets=Count(
            "training_sets", filter=Q(training_sets__released=True)
        ),
    )
    queryset = [obj for obj in queryset if obj.is_root_node() and obj.is_valid()]
    return queryset


def get_non_empty_disciplines(queryset):
    """
    Filters a discipline queryset so that every element recursively either have
    at least one sub-discipline or one training set.

    :param queryset: Queryset of `vocgui.Discipline` objects
    :type queryset: QuerySet
    :return: (filtered) queryset
    :rtype: QuerySet
    """
    queryset = [
        obj
        for obj in queryset
        if get_child_count(obj) > 0
        or obj.training_sets.filter(released=True).count() > 0
    ]
    return queryset


def check_group_object_permissions(request, group_id):
    """Function to check if the API-Key of the passed request object
    matches one of the hashed keys stored in the database of the
    corresponding group id.

    :param request: current request
    :type request: HttpRequest
    :param group_id: group id
    :type group_id: int
    :raises PermissionDenied: Exception if no API-Key is delivered
    :raises PermissionDenied: Exception if API-Key doesn't belong to passed group id
    """
    key = get_key(request)
    if not key:
        raise PermissionDenied()
    try:
        api_key_object = GroupAPIKey.objects.get_from_key(key)
    except GroupAPIKey.DoesNotExist:
        raise PermissionDenied()
    if int(api_key_object.organization_id) != int(group_id):
        raise PermissionDenied()
