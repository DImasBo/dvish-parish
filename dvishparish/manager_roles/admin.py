from django.contrib import admin

from .models import ResultDaily


@admin.register(ResultDaily)
class ResultDailyAdmin(admin.ModelAdmin):
    list_display = ["user", "KPI", "KPl_result_amount", "date_add", "date_update"]

    list_filter = ['KPI', "date_add"]
