from django.contrib import admin

from .models import ResultDaily, ResultItem


class ResultItemInline(admin.TabularInline):
    model = ResultItem
    extra = 0


@admin.register(ResultDaily)
class ResultDailyAdmin(admin.ModelAdmin):
    list_display = ["user", "date_add", "date_update"]
    list_filter = ["date_add"]
    inlines = [
        ResultItemInline,
    ]
