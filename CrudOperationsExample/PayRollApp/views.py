from typing import Dict
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Employee, PartTimeEmployee
from .forms import EmployeeForms, PartTimeEmployeeForm, PartTimeEmployeeFormSet
from django.core.paginator import Paginator, PageNotAnInteger
from django.conf import settings
from django.db.models import Q

# Create your views here.


def employee_list(request: HttpRequest) -> HttpResponse:
    # employees = Employee.objects.all()  # pyright: ignore
    employees = Employee.objects.select_related("emp_department", "emp_country").all()  # pyright: ignore
    print(employees.query)
    template_file = "PayRollApp/EmployeesList.html"
    context: Dict[str, list[Employee]] = dict({"Employees": employees})  # pyright: ignore
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
        PartTimeEmployeeForm(
            request.POST or None,  # pyright: ignore reportCallIssue
            prefix=f"employee-{i}",
        )
        for i in range(extra_forms)
    ]
    status = ""

    if request.method == "POST":
        for form in forms:
            if form.is_valid() and form.cleaned_data.get("first_name", ""):  # pyright: ignore reportAttributeAccessIssue
                form.save()  # pyright: ignore reportAttributeAccessIssue
                status = "Records were inserted successfully!!!"

    context = {"forms": forms, "extra_forms": range(extra_forms), "status": status}

    template = "PayRollApp/ParttimeEmployeeForm_list.html"

    return render(request=request, template_name=template, context=context)


def new_bulk_insert_demo(
    request: HttpRequest,
) -> HttpResponse | HttpResponseRedirect | None:
    if request.method == "POST":
        formset = PartTimeEmployeeFormSet(request.POST, prefix="employee")
        if formset.is_valid():
            employees = formset.save(commit=False)
            PartTimeEmployee.objects.bulk_create(employees)  # pyright: ignore
            return redirect("NewBulkInsert")
    else:
        formset = PartTimeEmployeeFormSet(
            queryset=PartTimeEmployee.objects.none(),  # pyright: ignore
            prefix="employee",
        )
        context = {"formset": formset}
        template = "PayRollApp/NewBulkInsert.html"
        return render(request=request, template_name=template, context=context)


def bulk_update_demo(request: HttpRequest) -> HttpResponse:
    employees = PartTimeEmployee.objects.all()  # pyright: ignore

    forms = [
        PartTimeEmployeeForm(
            request.POST or None,  # pyright: ignore
            instance=employee,
            prefix=f"employee-{employee.id}",  # pyright: ignore
        )
        for employee in employees
    ]

    if request.method == "POST":
        print("executando...")
        updated_data = []
        for form in forms:
            if form.is_valid():  # pyright:ignore
                print(form.is_valid())  # pyright:ignore
                print(form.instance)  # pyright:ignore
                employee = form.instance  # pyright: ignore
                employee.first_name = form.cleaned_data["first_name"]  # pyright: ignore
                employee.last_name = form.cleaned_data["last_name"]  # pyright: ignore
                employee.title_name = form.cleaned_data["title_name"]  # pyright: ignore
                updated_data.append(employee)
        print(updated_data)
        PartTimeEmployee.objects.bulk_update(  # pyright: ignore
            updated_data, ["first_name", "last_name", "title_name"]
        )

    return render(
        request, "PayRollApp/BulkUpdate.html", {"forms": forms, "employees": employees}
    )


def bulk_delete_demo(request: HttpRequest) -> HttpResponse:
    employees = PartTimeEmployee.objects.all()  # pyright:ignore
    if request.method == "POST":
        selected_ids = request.POST.getlist("selected_ids")
        print(selected_ids)
        if selected_ids:
            PartTimeEmployee.objects.filter(pk__in=selected_ids).delete()  # pyright:ignore
            return redirect("BulkDeleteDemo")
    return render(
        request=request,
        template_name="PayRollApp/BulkDelete.html",
        context={"employees": employees},
    )


def delete_using_radio(request: HttpRequest) -> HttpResponse:
    employees = PartTimeEmployee.objects.all()  # pyright: ignore  [reportAttributeAccessIssue]

    if request.method == "POST":
        selected_id = request.POST.get("selected_id")
        if selected_id:
            PartTimeEmployee.objects.filter(pk=selected_id).delete()  # pyright: ignore  [reportAttributeAccessIssue]
            return redirect("DeleteUsingRadio")

    return render(
        request=request,
        template_name="PayRollApp/DeleteUsingRadio.html",
        context={"employees": employees},
    )


def page_wise_employees_list(request: HttpRequest) -> HttpResponse:
    page_size = int(request.GET.get("page_size", getattr(settings, "PAGE_SIZE", 5)))  # pyright: ignore
    page = request.GET.get("page", 1)
    search_query = request.GET.get("search", "")

    # employees = PartTimeEmployee.objects.all()  # pyright: ignore
    sort_by = request.GET.get('sort_by', 'id')
    sort_order = request.GET.get('sort_order', 'asc')

    valid_sort_field = ['id', 'first_name', 'last_name', 'title_name']
    if sort_by not in valid_sort_field:
        sort_by = 'id'

    employees = PartTimeEmployee.objects.filter( # pyright: ignore 
        Q(id__icontains=search_query) |
        Q(first_name__icontains=search_query) |
        Q(last_name__icontains=search_query) |
        Q(title_name__icontains=search_query)
    )
        
    if sort_order == 'desc':
        employees = employees.order_by(f'-{sort_by}')
    else:
        employees = employees.order_by(sort_by)

    paginator = Paginator(employees, page_size)

    try:
        employees_page = paginator.page(page)
    except PageNotAnInteger:
        employees_page = paginator.page(1)

    return render(
        request,
        "PayRollApp/PageWiseEmployees.html",
        {
            "employees_page": employees_page, 
            "page_size": page_size,
            "search_query": search_query,
            "sort_by": sort_by,
            "sort_order": sort_order
        },
    )
