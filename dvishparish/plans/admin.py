from django.contrib import admin

from .forms import KPIForm
from .models import KPI, Formula, GeneralPlan, KPIitems, ManagerKPI, BankOfficeKPI


class KPIitemsInline(admin.TabularInline):
    model = KPIitems
    extra = 1


@admin.register(GeneralPlan)
class GeneralPlanAdmin(admin.ModelAdmin):
    list_display = ["date_from", "date_to"]
    inlines = [
        KPIitemsInline
    ]


@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    list_display = ["name","percentage_on_salary", "percentage_of_the_plan"]


@admin.register(KPI)
class KPIAdmin(admin.ModelAdmin):
    form = KPIForm
    list_display = ["indicator_name", "formula", "formula_bankoffice",
                    "target_amount","date_from","date_to"]
    list_filter = ['date_from','date_to', ]


@admin.register(ManagerKPI)
class ManagerKPIAdmin(admin.ModelAdmin):
    list_display = ["user", "KPI", "amount"]
    fieldsets = (
        (None, {
                'classes': ('wide',),
                'fields': ("user", "KPI", "amount")
            }), )


@admin.register(BankOfficeKPI)
class BankOfficeKPIAdmin(admin.ModelAdmin):
    list_display = ["bankoffice", "KPI", "amount"]
