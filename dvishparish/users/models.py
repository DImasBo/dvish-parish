from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

from dvishparish.manager_roles.roles import Finance, Manager, HR, Businesses, role_name_list

from rolepermissions.roles import assign_role

class BankOffice(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    city = models.CharField( blank=True, max_length=255)
    address = models.CharField( blank=True, max_length=255)

    def __str__(self):
        return f"№{self.id} {self.city} {self.address}"

class User(AbstractUser):
    """Default user for dvishparish."""

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    bankoffice =  models.ForeignKey(BankOffice, related_name='users', on_delete=models.CASCADE, null=True, blank=True) 
    salary = models.DecimalField( default=0, max_digits=8, decimal_places=2, null=True)

    def get_groups_display(self):
        return " ".join(self.groups.all().values_list('name',flat=True))

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

class AbstractPremia(models.Model):
    amount = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.user.__str__()} - {self.amount}UAH {self.date.strftime('%m/%d/%Y')}"

    class Meta:
        abstract = True
        

class Premia(AbstractPremia):
    user = models.ForeignKey(User, related_name='premias', on_delete=models.CASCADE)

class Bonus(AbstractPremia):
    user = models.ForeignKey(User, related_name='Bonus', on_delete=models.CASCADE)