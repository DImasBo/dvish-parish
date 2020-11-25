from django.contrib import admin

from .forms import KPIForm, ManagerKPIChannelForm
from .models import KPI, Formula, GeneralPlan, BankOfficePlan, ManagerPlan, \
                    ManagerKPI, BankOfficeKPI


@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    list_display = ["name","percentage_on_salary", "percentage_of_the_plan"]

@admin.register(KPI)
class KPIAdmin(admin.ModelAdmin):
    form = KPIForm
    list_display = ["indicator_name", "formula", "formula_bankoffice",
                    "target_amount","date_from","date_to"]
    list_filter = ['date_from','date_to', ]

@admin.register(GeneralPlan)
class GeneralPlanAdmin(admin.ModelAdmin):
    list_display = ["KPI"]
    # add_form = GeneralPlanCreationForm
    # add_fieldsets = (
    #     (None, {
    #             'classes': ('wide',),
    #             'fields': ("date_from", "date_to")
    #             }),
    #     ("KPI", {
    #         "fields": ("indicator_name","target_amount","formula_manager","formula_bankoffice")
    #         })
    # )

    # def get_fieldsets(self, request, obj=None):
    #     if not obj:
    #         return self.add_fieldsets
    #     return super().get_fieldsets(request, obj)

    # def get_form(self, request, obj=None, **kwargs):
    #     """
    #     Use special form during user creation
    #     """
    #     defaults = {}
    #     if obj is None:
    #         defaults['form'] = self.add_form
    #     defaults.update(kwargs)
    #     return super().get_form(request, obj, **defaults)

@admin.register(ManagerKPI)
class ManagerKPIAdmin(admin.ModelAdmin):
    form = ManagerKPIChannelForm
    list_display = ["user", "KPI", "amount"]
    fieldsets = (
        (None, {
                'classes': ('wide',),
                'fields': ("user", "KPI", "amount")
            }), )

@admin.register(BankOfficeKPI)
class BankOfficeKPIAdmin(admin.ModelAdmin):
    list_display = ["bankoffice", "KPI", "amount"]

# @admin.register(BankOfficePlan)
# class BankOfficePlanAdmin(admin.ModelAdmin):
#     list_display = ["bankoffice", "general_plan", "KPI", "amount"]


# @admin.register(ManagerPlan)
# class ManagerPlanAdmin(admin.ModelAdmin):
#     list_display = ["user", "general_plan", "KPI", "amount"]
