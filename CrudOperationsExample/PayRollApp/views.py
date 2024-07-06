from typing import Dict
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .models import Employee
from .forms import EmployeeForms

# Create your views here.


def employee_list(request: HttpRequest) -> HttpResponse:
    # employees = Employee.objects.all()  # pyright: ignore
    employees = Employee.objects.select_related("emp_department", "emp_country").all()  # pyright: ignore
    print(employees.query)
    template_file = "PayRollApp/EmployeesList.html"
    context: Dict[str, list[Employee]] = dict({"Employees": employees})
    return render(request=request, template_name=template_file, context=context)  # noqa


def employee_details(request: HttpRequest, id: int) -> HttpResponse:
    template_file = "PayRollApp/EmployeeDetails.html"
    # employee: Employee = Employee.objects.get(id=id)  # pyright: ignore
    employee: Employee = (
        Employee.objects.select_related("emp_department", "emp_country")  # pyright: ignore
        .all()
        .filter(id=id)
    )[0]
    context: Dict[str, Employee] = {"Employee": employee}
    return render(request=request, template_name=template_file, context=context)  # noqa


def employee_delete(request: HttpRequest, id: int) -> HttpResponse:
    template_file = "PayRollApp/EmployeeDelete.html"
    employee: Employee = Employee.objects.get(id=id)  # pyright:ignore
    context: Dict[str, Employee] = {"Employee": employee}
    if request.method == "POST":
        employee.delete()
        return redirect("EmployeeList")
    return render(request=request, template_name=template_file, context=context)  # noqa


def employee_update(request: HttpRequest, id: int) -> HttpResponse:
    template_file = "PayRollApp/EmployeeUpdate.html"
    employee = Employee.objects.get(id=id)  # pyright: ignore
    form = EmployeeForms(instance=employee)  # create a form based model from employee
    context: Dict[str, EmployeeForms] = {"form": form}
    if request.method == "POST":
        form = EmployeeForms(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect("EmployeeList")

    return render(request=request, template_name=template_file, context=context)


def employee_insert(request: HttpRequest) -> HttpResponse:
    template_file = "PayRollApp/EmployeeInsert.html"
    form = EmployeeForms()
    if request.method == "POST":
        form = EmployeeForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("EmployeeList")

    return render(request, template_file, {"form": form})
