from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.mixins import HasRoleMixin

from dvishparish.plans.models import ManagerKPI, BankOfficePlan
from .models import ResultDaily


class IndexManagerView(HasRoleMixin, LoginRequiredMixin, TemplateView):
    """Render Dashboard page."""
    template_name = "roles/manager/index.html"
    allowed_roles = 'manager'


class ManagerKPIsView(HasRoleMixin, LoginRequiredMixin, ListView):
    """Render Dashboard page."""
    template_name = "roles/manager/KPIs.html"
    allowed_roles = 'manager'
    model = ManagerKPI
    paginate_by = 30

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class ResultDailyView(HasRoleMixin, LoginRequiredMixin, ListView):
    template_name = "roles/manager/result.html"
    model = ResultDaily
    paginate_by = 30
    allowed_roles = 'manager'


class BankOfficePlansView(HasRoleMixin, LoginRequiredMixin, ListView):
    """Render Dashboard page."""
    template_name = "roles/manager/bankoffice_plans.html"
    allowed_roles = 'manager'
    model = BankOfficePlan
    paginate_by = 30

    def get_queryset(self):
        return self.model.objects.filter(
            bankoffice=self.request.user.bankoffice)
