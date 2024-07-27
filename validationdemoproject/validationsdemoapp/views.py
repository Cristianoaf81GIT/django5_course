from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from validationsdemoapp.forms import UserRegistrationForm

# Create your views here.
def sign_up(request: HttpRequest) -> HttpResponse:
    form = UserRegistrationForm()
    return render(request=request, template_name="validationsdemoapp/signup.html", context={"form": form})

