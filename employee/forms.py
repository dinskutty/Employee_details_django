from django import forms
from employee.models import Employ

class EmployForm(forms.ModelForm):
    class Meta:
        model=Employ
        fields="__all__"