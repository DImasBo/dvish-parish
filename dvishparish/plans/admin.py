from django.contrib import admin

from .forms import GeneralPlanCreationForm
from .models import KPI, Formula, GeneralPlan, KPIitem, BankOfficePlan, ManagerPlan


class KPIitemInline(admin.TabularInline):
	model = KPIitem

@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
	list_display = ["name","percentage_on_salary", "percentage_of_the_plan"]

@admin.register(KPI)
class KPIAdmin(admin.ModelAdmin):
	list_display = ["indicator_name"]

@admin.register(GeneralPlan)
class GeneralPlanAdmin(admin.ModelAdmin):
	list_display = ["date_from","date_to", "KPI"]
	add_form = GeneralPlanCreationForm
	add_fieldsets = (
		(None, { 
            	'fields': ("date_to")
            	}),
	)

@admin.register(BankOfficePlan)
class BankOfficePlanAdmin(admin.ModelAdmin):
	list_display = ["bankoffice", "general_plan", "KPI", "amount"]


@admin.register(ManagerPlan)
class ManagerPlanAdmin(admin.ModelAdmin):
	list_display = ["user", "general_plan", "KPI", "amount"]
