from dvishparish.plans.models import KPI
from dvishparish.manager_roles.models import ResultItem
from dvishparish.users.models import User
from django.utils import timezone


def get_sum_result_by_KPI_and_user(user: User, kpi:KPI):
    """ get sum result User with KPI """
    today = timezone.now()
    qs = ResultItem.objects.filter(
        result_daily__date_add__lte=today,
        result_daily__date_add__gte=kpi.date_from,
        result_daily__user=user,
        KPI=kpi
    )
    return sum(qs.values_list("KPI_result_amount", flat=True))


def get_сurrent_manager_kpis(user):
    today = timezone.now()
    KPIs = user.manager_kpis.filter(
        user=user,
        KPI__date_from__lte=today,
        KPI__date_to__gte=today,
    )
    return KPIs