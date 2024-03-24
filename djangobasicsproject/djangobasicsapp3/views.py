from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def Home(request: HttpRequest) -> HttpResponse:
    template_file_name = "djangobasicsapp3/Home.html"
    return render(request=request, template_name=template_file_name)
