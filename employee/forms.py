from django import forms

from .models import Employee


class SearchForm(forms.Form):

    department = forms.ModelChoiceField(
        queryset=Employee.objects, label="DTE", required=False
    )
