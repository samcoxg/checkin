from django import forms
from django.db.models import fields
from .models import *


class DateInput(forms.DateTimeInput):
    input_type = 'time'


class MilkFeedingModelForm(forms.ModelForm):
    class Meta:
        model = MilkFeeding
        fields = ['ate_at', 'total_amount', 'formula_type', 'formula_percent']
        widgets = {
            'ate_at': DateInput(),
        }
