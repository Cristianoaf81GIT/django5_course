from django import forms
from django.core.validators import re

from validationsdemoapp.models import UserRegistration


class UserRegistrationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if not isinstance(visible.field.widget, forms.RadioSelect) and not isinstance(visible.field.widget, forms.CheckboxInput):
                visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = UserRegistration
        fields = "__all__"

        genders = [{"male","Male"},{"female", "Female"}]
        countries = [
            ("select", "Please Choose Country"),
            ("India", "india"),
            ("Autralia", "australia"),
            ("America", "America"),
            ("Spain", "Spain")
        ]

        widgets = {
            "password": forms.PasswordInput(),
            "confirm_password": forms.PasswordInput(),
            "gender": forms.RadioSelect(choices=genders),
            "country": forms.Select(choices=countries),
            "email": forms.EmailInput(),
            "website_url": forms.URLInput(),
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "terms_conditions": forms.CheckboxInput()
        }
    
    def clean_phone_number(self) -> str | None:
        """Field validation method, validates user phone number
           
           Returs:
               str | None: string with validated phone number or none 
        """

        phone_data: None | str = self.cleaned_data.get("phone_number")
        if phone_data:
            pattern = re.compile(r"(0|91)?[6-9][0-9]{9}")
            if not re.fullmatch(pattern, phone_data):
                raise forms.ValidationError("Ivalid phone number! Example: +916234567891")
            return phone_data
