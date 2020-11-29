from typing import Any
from django.urls import reverse

from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.http import HttpRequest


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    def get_login_redirect_url(self, request):
        """Redirect superusers and affiliates to user list in admin panel."""
        user = self.request.user
        url = settings.LOGIN_REDIRECT_URL

        if request.user.is_staff and not request.user.groups.filter(name="manager").exists():
            return reverse('admin:index')
        return super().get_login_redirect_url(request)

