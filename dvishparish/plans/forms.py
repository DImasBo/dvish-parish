from django import forms
from .models import Formula, KPI, ManagerKPI
#from .utils import get_bankoffice_amounts
from django.core.exceptions import ValidationError


class KPIForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['formula'].queryset = Formula.objects.filter(is_bankoffice=False)
        self.fields['formula_bankoffice'].queryset = Formula.objects.filter(is_bankoffice=True)

    class Meta:
        model = KPI
        fields = "__all__"

