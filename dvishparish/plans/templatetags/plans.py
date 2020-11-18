from django import template
from dvishparish.plans.utils import get_сurrent_manager_plans, get_current_bankoffice_plans

register = template.Library()

@register.filter(name='current_manager_plans')
def tag_get_current_manager_plans(user):
	return get_сurrent_manager_plans(user)

@register.filter(name='current_bankoffice_plans')
def tag_get_current_manager_plans(user):
	return get_current_bankoffice_plans(user)
