from django.http import HttpResponse
from django.shortcuts import render
from django.test.client import HttpRequest

# Create your views here.

def Home(request: HttpRequest) -> HttpResponse:
    template_file_name = "djangobasicsapp2/Home.html"
    return render(request=request, template_name=template_file_name)
