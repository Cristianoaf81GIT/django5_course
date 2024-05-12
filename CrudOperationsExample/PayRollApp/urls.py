from django.urls import path


from . import views

urlpatterns = [path("EmployeeList", views.employee_list, name="EmployeeList")]
