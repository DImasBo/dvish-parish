from django.db import models
from dvishparish.users.models import User, BankOffice
from django.contrib.auth import get_user_model
from django.utils import timezone

from django.core.validators import MaxValueValidator, MinValueValidator


class Formula(models.Model):
    name = models.CharField(max_length=150)
    percentage_on_salary = models.DecimalField(
        default=20,
        max_digits=8,
        decimal_places=2,
        validators=[
            MinValueValidator(1)
        ])

    percentage_of_the_plan = models.DecimalField(
        default=100,
        max_digits=8,
        decimal_places=2,
        validators=[
            MinValueValidator(100)
        ])
    is_bankoffice = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - Відсоток премії {self.percentage_on_salary}%. Виконати план на {self.percentage_of_the_plan}%"


class KPI(models.Model):
    is_general_plan = models.BooleanField(default=False)
    indicator_name = models.CharField(max_length=150)
    formula = models.ForeignKey(Formula, related_name='KPIs', on_delete=models.CASCADE, null=True, blank=True)
    formula_bankoffice = models.ForeignKey(Formula, related_name='KPIs_b', on_delete=models.CASCADE, null=True, blank=True)

    target_amount = models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        validators=[
            MinValueValidator(0)
        ])

    date_from = models.DateTimeField(default=timezone.now())
    date_to = models.DateTimeField()
    
    class Meta:
        unique_together = ("formula", "formula_bankoffice")

    def __str__(self):
        return f"{self.indicator_name} | {self.date_from} - {self.date_to} {self.target_amount}"


class GeneralPlan(models.Model):
    date_from = models.DateTimeField(default=timezone.now())
    date_to = models.DateTimeField()

    def __str__(self):
        return f"{self.date_from} - {self.date_to}"


class KPIitem(models.Model):
    KPI = models.ForeignKey(KPI, related_name='kpi_items', on_delete=models.CASCADE)
    general_plan = models.ForeignKey(GeneralPlan, related_name="kpi_items", on_delete=models.CASCADE)

class BankOfficeKPI(models.Model):
    bankoffice = models.ForeignKey(BankOffice, related_name='bankoffice_kpis', on_delete=models.CASCADE)
    KPI = models.ForeignKey(KPI, related_name='bankoffice_kpis' , on_delete=models.CASCADE, blank=True, null=True)
    amount =  models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        validators=[
            MinValueValidator(0)
        ])

    def __str__(self):
        return f"{self.KPI.__str__()} | {self.bankoffice.__str__()} - {self.amount}"


class ManagerKPI(models.Model):
    user = models.ForeignKey(User,  related_name='manager_kpis', on_delete=models.CASCADE)
    KPI = models.ForeignKey(KPI, related_name='manager_kpis' , on_delete=models.CASCADE, blank=True, null=True)
    amount =  models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        validators=[
            MinValueValidator(0)
        ])

    def __str__(self):
        return f"{self.KPI.__str__()} | {self.user.__str__()} - {self.amount}"
