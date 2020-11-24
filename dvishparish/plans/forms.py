from django import forms
from .models import GeneralPlan, Formula, KPI

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
        print(self.fields)
        self.fields['formula'].queryset = Formula.objects.filter(is_bankoffice=False)
        self.fields['formula_bankoffice'].queryset = Formula.objects.filter(is_bankoffice=True)
        print(self.fields['formula_bankoffice'].queryset)

    class Meta:
        model = KPI
        fields = "__all__"