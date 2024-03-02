from django import forms

from .models import Employee


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class SearchForm(forms.Form):

    department = forms.ModelChoiceField(
        queryset=Employee.objects, label="DTE", required=False
    )
