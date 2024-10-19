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
    path("BulkEmployeeDemo", views.bulk_insert_demo, name="BulkEmployeeDemo"),
    path("NewBulkInsert", views.new_bulk_insert_demo, name="NewBulkInsert"),
    path("BulkUpdate", views.bulk_update_demo, name="BulkUpdate"),
    path("BulkDeleteDemo", views.bulk_delete_demo, name="BulkDeleteDemo"),
]
