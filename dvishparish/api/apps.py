from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class APIConfig(AppConfig):
    name = "dvishparish.api"
    verbose_name = _("API")
