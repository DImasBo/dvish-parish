from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.mixins import HasRoleMixin

from dvishparish.plans.models import ManagerPlan, BankOfficePlan


class IndexManagerView(HasRoleMixin, LoginRequiredMixin, TemplateView):
    """Render Dashboard page."""
    template_name = "roles/manager/index.html"
    allowed_roles = 'manager'


class ManagerPlansView(HasRoleMixin, LoginRequiredMixin, ListView):
    """Render Dashboard page."""
    template_name = "roles/manager/self_plans.html"
    allowed_roles = 'manager'
    model = ManagerPlan
    paginate_by = 30

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class BankOfficePlansView(HasRoleMixin, LoginRequiredMixin, ListView):
    """Render Dashboard page."""
    template_name = "roles/manager/bankoffice_plans.html"
    allowed_roles = 'manager'
    model = BankOfficePlan
    paginate_by = 30

    def get_queryset(self):
        return self.model.objects.filter(
            bankoffice=self.request.user.bankoffice)
