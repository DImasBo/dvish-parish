from django.db import models
from users.models import User, BankOffice

class Product(models.Model):
    name = models.CharField(max_length=150)

class AbstractPlan:
    amount = models.PositiveIntegerField()
    class Meta:
        abstract = True

class GeneralPlan(AbstractPlan): 
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    product = models.ForeignKey(Product, related_name='generals_plans' , on_delete=models.CASCADE) 

class OfficePlan(AbstractPlan):
    general_plan = models.ForeignKey(GeneralPlan, related_name='offices_plans', on_delete=models.CASCADE)
    office = models.ForeignKey(BankOffice, related_name='offices_plans', on_delete=models.CASCADE)

class ManagerPlan(AbstractPlan):
    general_plan = models.ForeignKey(GeneralPlan, related_name='manager_plans', on_delete=models.CASCADE)
    user = models.ForeignKey(User,  related_name='manager_plans', on_delete=models.CASCADE)
