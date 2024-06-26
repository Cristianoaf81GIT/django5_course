from django.urls import path


from . import views

urlpatterns = [
    path("EmployeeList", views.employee_list, name="EmployeeList"),
    path(
        "EmployeeDetails/<int:id>",
        views.employee_details,
        name="EmployeeDetails",  # noqa
    ),  # noqa
    path("EmployeeDelete/<int:id>", views.employee_delete, name="EmployeeDelete"),  # noqa
    path("EmployeeUpdate/<int:id>", views.employee_update, name="EmployeeUpdate"),
    path("EmployeeInsert", views.employee_insert, name="EmployeeInsert"),
]
