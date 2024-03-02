from django import forms

from .models import DTE


class SearchForm(forms.Form):

    department = forms.ModelChoiceField(
        queryset=DTE.objects, label="部署", required=False
    )
