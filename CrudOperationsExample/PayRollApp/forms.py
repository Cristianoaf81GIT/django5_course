from django import forms
from django.forms import Select, TextInput, modelform_factory
from .models import Employee, OnSiteEmployees, PartTimeEmployee



# creating a form based model
class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = { #noqa
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

PartTimeEmployeeForm = modelform_factory(PartTimeEmployee, fields=['first_name', 'last_name', 'title_name'])

class DynamicPartTimeEmployeeForm(PartTimeEmployeeForm):

    def __init__(self, *args, **kwargs) -> None:
        super(PartTimeEmployeeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values(): # pyright: ignore reportAttributeAccessIssue
            field.widget.attrs.pop("required", None)



class NewPartTimeEmployeeForm(forms.ModelForm):

    class Meta:
        model=PartTimeEmployee
        fields="__all__" 


PartTimeEmployeeFormSet = forms.modelformset_factory(PartTimeEmployee, form=NewPartTimeEmployeeForm, extra=10)


class OnSiteEmployeesForm(forms.ModelForm):
    class Meta:
        model = OnSiteEmployees
        fields = ['first_name', 'last_name', 'country', 'state', 'city']

        widgets = { # noqa
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
            }),
            'country': Select(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Country',
            }),
            'state': Select({
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'State',
            }),
            'city': Select(attrs={                
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'State',
            })
        }



