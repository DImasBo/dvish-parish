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
        return f"{self.name} - {self.percentage_on_salary} {self.percentage_of_the_plan}"

class KPI(models.Model):
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
        return self.indicator_name

class GeneralPlan(models.Model):

    KPI = models.ForeignKey(KPI, related_name='generals_plans' , on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.KPI.__str__()} | {self.date_from} - {self.date_to}"

class BankOfficePlan(models.Model):
    general_plan = models.ForeignKey(GeneralPlan, related_name='bankoffice_plans', on_delete=models.CASCADE)
    bankoffice = models.ForeignKey(BankOffice, related_name='bankoffice_plans', on_delete=models.CASCADE)
    KPI = models.ForeignKey(KPI, related_name='bankoffice_plans' , on_delete=models.CASCADE, blank=True, null=True)
    amount =  models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        validators=[
        MinValueValidator(0)
        ])

    def __str__(self):
        return f"{self.KPI.__str__()} | {self.bankoffice.__str__()} - {self.amount} | {self.general_plan.__str__()}"

class ManagerPlan(models.Model):
    general_plan = models.ForeignKey(GeneralPlan, related_name='manager_plans', on_delete=models.CASCADE)
    user = models.ForeignKey(User,  related_name='manager_plans', on_delete=models.CASCADE)
    KPI = models.ForeignKey(KPI, related_name='manager_plans' , on_delete=models.CASCADE, blank=True, null=True)
    amount =  models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        validators=[
        MinValueValidator(0)
        ])
    def __str__(self):
        return f"{self.KPI.__str__()} | {self.user.__str__()} - {self.amount} | {self.general_plan.__str__()}"

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
