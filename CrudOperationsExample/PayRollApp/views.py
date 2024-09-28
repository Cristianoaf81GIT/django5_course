from typing import Dict
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.http import HttpRequest, HttpResponse
from .models import Employee, PartTimeEmployee
from .forms import EmployeeForms, PartTimeEmployeeForm, PartTimeEmployeeFormSet

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
    # employee: Employee = Employee.objects.get(id=id)  # pyright:ignore
    employee: Employee = (
        Employee.objects.select_related("emp_department", "emp_country")  # pyright:ignore
        .all()
        .filter(id=id)[0]
    )
    context: Dict[str, Employee] = {"Employee": employee}
    if request.method == "POST":
        employee.delete()
        return redirect("EmployeeList")
    return render(request=request, template_name=template_file, context=context)  # noqa


def employee_update(request: HttpRequest, id: int) -> HttpResponse:
    template_file = "PayRollApp/EmployeeUpdate.html"
    employee = (
        Employee.objects.select_related("emp_department", "emp_country")  # pyright: ignore
        .all()
        .filter(id=id)
    )

    emp_data = employee[0] or None
    form = EmployeeForms(instance=emp_data)  # create a form based model from employee

    context: Dict[str, EmployeeForms] = {"form": form}

    #    for emp in employee:
    #        emp_data = emp
    #        form = EmployeeForms(
    #            instance=emp_data
    #        )  # create a form based model from employee
    #        context = {"form": form}

    if request.method == "POST":
        form = EmployeeForms(request.POST, instance=emp_data)
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

def bulk_insert_demo(request: HttpRequest) -> HttpResponse:
    extra_forms = 10
    forms = [
        PartTimeEmployeeForm(request.POST or None, #pyright: ignore reportCallIssue
        prefix=f"employee-{i}") for i in range(extra_forms)
    ]
    status = "" 

    
    if request.method == "POST":
        for form in forms:
            if form.is_valid() and form.cleaned_data.get("first_name", ""): #pyright: ignore reportAttributeAccessIssue
                form.save() #pyright: ignore reportAttributeAccessIssue
                status = "Records were inserted successfully!!!"

    context = {
        "forms": forms,
        "extra_forms": range(extra_forms),
        "status": status
    }

    template = "PayRollApp/ParttimeEmployeeForm_list.html" 

    return render(request=request, template_name=template, context=context)


def new_bulk_insert_demo(request: HttpRequest) -> HttpResponse | HttpResponseRedirect | None:
    if request.method == "POST":
        formset = PartTimeEmployeeFormSet(request.POST, prefix="employee")
        if formset.is_valid():
            employees = formset.save(commit=False)
            PartTimeEmployee.objects.bulk_create(employees) #pyright: ignore
            return redirect("NewBulkInsert")
    else:
        formset = PartTimeEmployeeFormSet(queryset=PartTimeEmployee.objects.none(), prefix="employee") # pyright: ignore [reportAttributeAccessIssue
        context = {"formset": formset}                                                                                    
        template="PayRollApp/NewBulkInsert.html"
        return render(request=request,template_name=template,context=context)


