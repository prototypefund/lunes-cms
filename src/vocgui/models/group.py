from django.contrib.auth.models import Group
from django.db import models
from .static import convert_umlaute_images
from django.utils.translation import ugettext_lazy as _

Group.add_to_class(
    "icon",
    models.ImageField(
        upload_to=convert_umlaute_images, blank=True, verbose_name=_("icon")
    ),
)
