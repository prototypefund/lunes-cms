from .discipline_filtered_viewset import DisciplineFilteredViewSet
from .discipline_viewset import DisciplineViewSet
from .document_by_id_viewset import DocumentByIdViewSet
from .document_viewset import DocumentViewSet
from .group_viewset import GroupViewSet
from .training_set_viewset import TrainingSetViewSet
from .other_viewset import public_upload, redirect_view

__all__ = [
    "DisciplineFilteredViewSet",
    "DisciplineViewSet",
    "DocumentByIdViewSet",
    "DocumentViewSet",
    "GroupViewSet",
    "TrainingSetViewSet",
    "public_upload",
    "redirect_view",
]
