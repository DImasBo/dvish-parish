from django.db import models
from dvishparish.users.models import User, BankOffice
from datetime import datetime

class KPI(models.Model):
    indicator_name = models.CharField(max_length=150)

    def __str__(self):
        return self.indicator_name

class GeneralPlan(models.Model): 
    date_from = models.DateTimeField(default=datetime.now())
    date_to = models.DateTimeField()
    KPI = models.ForeignKey(KPI, related_name='generals_plans' , on_delete=models.CASCADE)
    KPI_target_amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.KPI.__str__()} | {self.date_from} - {self.date_to} | {self.KPI_target_amount}"

class BankOfficePlan(models.Model):
    general_plan = models.ForeignKey(GeneralPlan, related_name='bankoffice_plans', on_delete=models.CASCADE)
    bankoffice = models.ForeignKey(BankOffice, related_name='bankoffice_plans', on_delete=models.CASCADE)
    KPI = models.ForeignKey(KPI, related_name='bankoffice_plans' , on_delete=models.CASCADE) 
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.KPI.__str__()} | {self.bankoffice.__str__()} - {self.amount} | {self.general_plan.__str__()}"

class ManagerPlan(models.Model):
    general_plan = models.ForeignKey(GeneralPlan, related_name='manager_plans', on_delete=models.CASCADE)
    user = models.ForeignKey(User,  related_name='manager_plans', on_delete=models.CASCADE)
    KPI = models.ForeignKey(KPI, related_name='manager_plans' , on_delete=models.CASCADE) 
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.KPI.__str__()} | {self.user.__str__()} - {self.amount} | {self.general_plan.__str__()}"
