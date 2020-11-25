from django.utils import timezone
from .models import ManagerPlan, ManagerKPI, GeneralPlan, BankOfficeKPI

def get_сurrent_manager_kpis(user):
	today = timezone.now()

	plans = ManagerKPI.objects.filter(
		user=user,
		KPI__date_from__lte=today,
		KPI__date_to__gte=today,
		)

	return  plans

def get_current_bankoffice_kips(user):
	today = timezone.now()

	plans = BankOfficeKPI.objects.filter(
		bankoffice=user.bankoffice,
		KPI__date_from__lte=today,
		KPI__date_to__gte=today
		)

	return  plans

# def get_kpi_daily(user):
# 	today = timezone.now()

# 	general_plans = GeneralPlan.objects.filter(
# 		date_from__lte=today,
# 		date_to__gte=today
# 		)

# 	plans = ManagerKPI.objects.filter(
# 		user__bankoffice=user.bankoffice,
# 		KPI__generals_plans__in=general_plans,
# 		)

# 	manager_kpi.KPI.target_amount
# 	tasks = []
# 	for plan in plans:
# 		general_plan = plan.KPI.generals_plans.filter(
# 			date_from__lte=today,
# 			date_to__gte=today)

# 		tasks.append({
# 			"KPI":plan.KPI,
# 			"amount":manager_kpi.KPI.target_amount /
# 		})
# 	return tasks

# def get_kpi_daily(manager_plan):
# 	delta_day = manager_plan.general_plan.date_from - manager_plan.general_plan.date_from
# 	print(delta_day)
	# dayli_plan =

def get_bankoffice_amounts(instance: ManagerKPI):
	use_amount = ManagerKPI.objects.filter(
		KPI=instance.KPI,
		user__bankoffice=instance.user.bankoffice).values_list("amount" ,flat=True)
	# print(l)

	return {
		"max_amount":instance.user.bankoffice.bankoffice_kpis.first().amount,
		"use_amount":sum(list(use_amount))
		}
