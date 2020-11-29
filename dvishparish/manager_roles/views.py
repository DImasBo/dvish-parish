from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.mixins import HasRoleMixin
from dvishparish.utils.manager import get_top_5_menegers_with_general_plan
from dvishparish.plans.models import ManagerKPI, KPI
from .models import ResultDaily


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


class Top5ManagersView(HasRoleMixin, LoginRequiredMixin, TemplateView):
    """Render Dashboard page."""
    template_name = "roles/manager/top5_managers.html"
    allowed_roles = 'manager'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tops'] = get_top_5_menegers_with_general_plan(self.request.user)
        print(context)
        return context


class ListKPIView(HasRoleMixin, LoginRequiredMixin, ListView):
    model = ManagerKPI
    allowed_roles = 'manager'
    template_name = "roles/manager/kpis_list.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)