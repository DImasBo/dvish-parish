from typing import Any

from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.http import HttpRequest


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest):
        if request.user.is_staff and not request.user.groups.get(name="manager").exists():
            return
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)