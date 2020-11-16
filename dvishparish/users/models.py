from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models


class BankOffice(models.Model):
    number = models.PositiveIntegerField()
    address = models.CharField(_("Name of User"), blank=True, max_length=255)
    city = models.CharField(_("Name of User"), blank=True, max_length=255)

class User(AbstractUser):
    """Default user for dvishparish."""

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    office =  models.ForeignKey(BankOffice, related_name='users', on_delete=models.CASCADE, null=True, blank=True) 

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})