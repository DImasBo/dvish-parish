from django.contrib import admin

from .models import KPI, GeneralPlan, BankOfficePlan, ManagerPlan


@admin.register(KPI)
class KPIAdmin(admin.ModelAdmin):
	list_display = ["id","indicator_name"]

@admin.register(GeneralPlan)
class GeneralPlanAdmin(admin.ModelAdmin):
	list_display = ["id","date_from","date_to", "KPI", "KPI_target_amount"]

@admin.register(BankOfficePlan)
class BankOfficePlanAdmin(admin.ModelAdmin):
	list_display = ["id", "bankoffice", "general_plan", "KPI", "amount"]


@admin.register(ManagerPlan)
class ManagerPlanAdmin(admin.ModelAdmin):
	list_display = ["id", "user", "general_plan", "KPI", "amount"]
