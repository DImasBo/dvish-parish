from django.utils import timezone
from .models import ManagerPlan

def get_сurrent_manager_plans(user):
	today = timezone.now()
	
	return user.manager_plans.filter(
		general_plan__date_from__lte=today, 
		general_plan__date_to__gte=today
		)

def get_current_bankoffice_plans(user):
	today = timezone.now()

	plans = ManagerPlan.objects.filter(
		user__bankoffice=user.bankoffice,
		general_plan__date_from__lte=today, 
		general_plan__date_to__gte=today
		)

	plans_amount = plans.values_list("amount",flat=True)
	plans_KPIs = plans.values_list("general_plan__KPI__indicator_name",flat=True)


	print(plans_amount)
	print(plans_KPIs)
	return  

def get_kpi_daily(manager_plan):
	delta_day = manager_plan.general_plan.date_from - manager_plan.general_plan.date_from 
	print(delta_day)
	# dayli_plan = 