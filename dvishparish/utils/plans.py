from django.utils import timezone

def get_сurrent_manager_kpis(user):
    today = timezone.now()
    KPIs = user.manager_kpis.filter(
        user=user,
        KPI__date_from__lte=today,
        KPI__date_to__gte=today,
    )
    return KPIs