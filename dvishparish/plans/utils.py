from datetime import datetime

def get_сurrent_manager_plans(user):
	today = datetime.now()
	
	return user.manager_plans.filter(
		general_plan__date_from__lte=today, 
		general_plan__date_to__gte=today
		)

def get_current_bankoffice_plans(user):
	today = datetime.now()
	
	return user.bankoffice.bankoffice_plans.filter(
		general_plan__date_from__lte=today, 
		general_plan__date_to__gte=today
		)
