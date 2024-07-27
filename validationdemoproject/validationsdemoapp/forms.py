from django import forms

from validationsdemoapp.models import UserRegistration


class UserRegistrationForm(forms.ModelForm):


    class Meta:
        model = UserRegistration
        fields = "__all__"
