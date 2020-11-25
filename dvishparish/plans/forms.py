from django import forms
from .models import GeneralPlan, Formula, KPI, ManagerKPI
from .utils import get_bankoffice_amounts
from django.core.exceptions import ValidationError


class GeneralPlanCreationForm(forms.ModelForm):

    indicator_name = forms.CharField()
    formula_manager = forms.ModelChoiceField(queryset=Formula.objects.all())
    formula_bankoffice = forms.ModelChoiceField(queryset=Formula.objects.all())
    target_amount = forms.FloatField( widget=forms.NumberInput(attrs={'min':1}) )

    def save(self, commit=False):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance

        # date_from = models.DateTimeField(default=timezone.now(), null=True, blank=True)
        # date_to = models.DateTimeField(null=True, blank=True)

    class Meta:
        model = GeneralPlan
        fields = '__all__'


class KPIForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['formula'].queryset = Formula.objects.filter(is_bankoffice=False)
        self.fields['formula_bankoffice'].queryset = Formula.objects.filter(is_bankoffice=True)

    class Meta:
        model = KPI
        fields = "__all__"

class ManagerKPIChannelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            amounts = get_bankoffice_amounts(self.instance)
            available_amount = amounts["max_amount"] - amounts["use_amount"]
            self.fields['amount'].widget = forms.NumberInput(attrs={"min":0, "max":available_amount})
            self.fields['amount'].help_text=f'{amounts["max_amount"]} was assigned to the office. {amounts["use_amount"]} was used. The maximum value can be {available_amount}.'

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if self.instance:
            amounts = get_bankoffice_amounts(self.instance)
            available_amount = amounts["max_amount"] - amounts["use_amount"]
            if amount > available_amount:
                raise ValidationError(f'{amounts["max_amount"]} was assigned to the office. {amounts["use_amount"]} was used. The maximum value can be {available_amount}.')
        return amount

    class Meta:
        model = ManagerKPI
        fields = "__all__"
