from django import forms

from .models import Employee, Skill, Training


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        widgets = {"employee": forms.HiddenInput()}


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = "__all__"
