from django import forms
from django.forms import modelform_factory
from .models import Employee, PartTimeEmployee



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

PartTimeEmployeeForm = modelform_factory(PartTimeEmployee, fields=['first_name', 'last_name', 'title'])

class DynamicPartTimeEmployeeForm(PartTimeEmployeeForm):

    def __init__(self, *args, **kwargs) -> None:
        super(PartTimeEmployeeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values(): # pyright: ignore reportAttributeAccessIssue
            field.widget.attrs.pop("required", None)
