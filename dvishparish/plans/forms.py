from django import forms
from .models import GeneralPlan

class GeneralPlanCreationForm(forms.ModelForm):
    # indicator_name = forms.CharField()
    # formula = forms.ForeignKey(Formula, related_name='KPIs')
        
    # KPI_target_amount = forms.FloatField( widget=forms.NumberInput(attrs={'min':1}) )
        
        # date_from = models.DateTimeField(default=timezone.now(), null=True, blank=True)
        # date_to = models.DateTimeField(null=True, blank=True)

    class Meta:
        model = GeneralPlan
        fields = "__all__"