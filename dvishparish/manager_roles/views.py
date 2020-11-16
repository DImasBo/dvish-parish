from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.mixins import HasRoleMixin

class IndexManagerView(HasRoleMixin, LoginRequiredMixin, TemplateView):
	"""Render Dashboard page."""
	template_name = "roles/manager/index.html"
	allowed_roles = 'finance'