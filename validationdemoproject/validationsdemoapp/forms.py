from typing import Any 
from django import forms
from django.core.validators import re
from django.utils.translation import gettext 

from validationsdemoapp.models import UserRegistration


class UserRegistrationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if not isinstance(visible.field.widget, forms.RadioSelect) \
                    and not isinstance(visible.field.widget, forms.CheckboxInput):
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

    
    def clean(self) -> dict[Any, Any]:
        """Form level validation method, validates user password

            Todo:
                * create auxiliary functions to check user form data.

            returns:
                dict[Any,Any] : dictionary with form data.

        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        test_message = gettext("welcome")
        print("message -> ",test_message)

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Passwords does not match")
        else:
            raise forms.ValidationError("Password fields must not be empty")

        username = cleaned_data.get("username")
        user_password = cleaned_data.get("password")

        if user_password and username:
            if username == user_password:
                raise forms.ValidationError("User name and password should not be the same...")

        country = cleaned_data.get("country")

        if country == 'select':
            raise forms.ValidationError("Please select a country")

        terms_and_conditions = cleaned_data.get("terms_conditions")

        if not terms_and_conditions:
            raise forms.ValidationError("Please agree with terms and conditions!")

        return cleaned_data


