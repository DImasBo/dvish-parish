from dvishparish.plans.models import KPI, GeneralPlan
from dvishparish.manager_roles.models import ResultItem
from dvishparish.users.models import User
from django.utils import timezone


def get_sum_result_by_KPI_and_user(user: User, kpi: KPI):
    """ get sum result User with KPI """
    today = timezone.now()
    qs = ResultItem.objects.filter(
        result_daily__date_add__lte=today,
        result_daily__date_add__gte=kpi.date_from,
        result_daily__user=user,
        KPI=kpi
    ).distinct()
    return sum(qs.values_list("KPI_result_amount", flat=True))


def get_сurrent_manager_kpis(user):
    today = timezone.now()
    KPIs = user.manager_kpis.filter(
        user=user,
        KPI__date_from__lte=today,
        KPI__date_to__gte=today,
    ).distinct()
    return KPIs


def get_top_5_menegers_with_general_plan(user):
    kpis_id = GeneralPlan.objects.first().kpi_items.all().values_list("KPI", flat=True)

    KPIs_plan = KPI.objects.filter(id__in=kpis_id).distinct()
    managers = User.objects.filter(groups__name="manager").distinct()
    results = []
    for manager in managers:
        sum_kpis = 0
        for kpi in KPIs_plan:
            sum_kpis += get_sum_result_by_KPI_and_user(
                manager, kpi
            )
        if user.id ==manager.id:
            results.append({
                "sum_kpis": sum_kpis,
                "user": manager,
                "is_self": True
            })
        else:
            results.append({
                "sum_kpis": sum_kpis,
                "user": manager
            })

    sort_results = sorted(
        results,
        key=lambda result: result['sum_kpis'],
        reverse=True)

    print(sort_results)

    number = 0
    i = 0
    while number == 0 and i < len(sort_results):
        if sort_results[i].get("is_self"):
            number = i
        i += 1
    if number+1 > 5:
        sort_results[5] = sort_results[number]
        sort_results[5]['number'] = number + 1
        return sort_results[:6]
    return sort_results[:5]
