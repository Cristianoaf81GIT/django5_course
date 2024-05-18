from typing import Dict
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Employee

# Create your views here.


def employee_list(request: HttpRequest) -> HttpResponse:
    employees = Employee.objects.all()  # pyright: ignore
    template_file = "PayRollApp/EmployeesList.html"
    context: Dict[str, list[Employee]] = dict({"Employees": employees})
    return render(request=request, template_name=template_file, context=context)  # noqa


def employee_details(request: HttpRequest, id: int) -> HttpResponse:
    template_file = "PayRollApp/EmployeeDetails.html"
    employee: Employee = Employee.objects.get(id=id)  # pyright: ignore
    context: Dict[str, Employee] = {"Employee": employee}
    return render(request=request, template_name=template_file, context=context)  # noqa
