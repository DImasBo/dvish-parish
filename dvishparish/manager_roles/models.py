from django.db import models
from dvishparish.users.models import User
from dvishparish.plans.models import KPI
from django.core.validators import MinValueValidator


class ResultDaily(models.Model):
    user = models.ForeignKey(User, related_name="results_daily", on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


class ResultItem(models.Model):
    result_daily = models.ForeignKey(ResultDaily, related_name="results_items",
                                     on_delete=models.CASCADE)
    KPI = models.ForeignKey(KPI, related_name="results_items", on_delete=models.CASCADE)
    KPl_result_amount = models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2,
        validators=[
            MinValueValidator(1)
        ])
