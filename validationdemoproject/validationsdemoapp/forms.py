from django import forms

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
