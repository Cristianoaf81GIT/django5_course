from django import forms
from .models import Employee


# creating a form based model
class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            "birth_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "dd/mm/yyyy",
                    "class": "form-control",
                },
                format="%Y-%m-%d",
            ),  # pyright: ignore
            "hire_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "dd/mm/yyyy",
                    "class": "form-control",
                },
                format="%Y-%m-%d",
            ),
        }
