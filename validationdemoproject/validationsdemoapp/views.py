from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from validationsdemoapp.forms import UserRegistrationForm

# Create your views here.
def sign_up(request: HttpRequest) -> HttpResponse:
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            return render(request=request, template_name="validationsdemoapp/home.html")
        else:
            return render(request=request, template_name="validationsdemoapp/signup.html", context={"form": form})
    else:    
        form = UserRegistrationForm()
        return render(request=request, template_name="validationsdemoapp/signup.html", context={"form": form})

