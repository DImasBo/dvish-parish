from django import template
from dvishparish.utils.result import get_sum_result_by_KPI_and_user
from dvishparish.utils.plans import get_сurrent_manager_kpis

register = template.Library()


@register.filter(name='current_manager_KPIs')
def tag_get_current_manager_plans(user):
	return get_сurrent_manager_kpis(user)


@register.simple_tag
def get_sum_result_user_kpi(user, kpi):
	return get_sum_result_by_KPI_and_user(user, kpi)