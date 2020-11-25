from django import template
from dvishparish.plans.utils import get_сurrent_manager_kpis, get_current_bankoffice_kips

register = template.Library()

@register.filter(name='current_manager_plans')
def tag_get_current_manager_plans(user):
	return get_сurrent_manager_kpis(user)

@register.filter(name='current_bankoffice_plans')
def tag_get_current_manager_plans(user):
	return get_current_bankoffice_kips(user)

@register.simple_tag
def get_all_current_KPIs(user):
	KPIs = {}
	BO_KPI = get_current_bankoffice_kips(user)

	M_KPI = get_сurrent_manager_kpis(user)

	if BO_KPI:
		KPIs['bankoffice_KPIs'] = BO_KPI
		KPIs['M_KPI']
