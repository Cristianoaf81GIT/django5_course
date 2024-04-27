from django.urls import path, URLResolver, URLPattern
from . import views
from typing import Final

urlpatterns: Final[list[URLResolver | URLPattern]] = [
    path("", views.Index, name="Index"),
    path("Index", views.Index, name="Index"),
    path("Home", views.Home, name="Home"),
    path("ShowMessages", views.ShowMoreMessage, name="SM"),
    path("UseVariables", views.UseVariableAsResponse, name="UVR"),
    path("GetRequestDemo", views.GetRequestVariables, name="GRV"),
    path("ShowTime", views.ShowDateTimeInfo, name="SDTI"),
    path("LoggingDemo", views.LoggingExample, name="LoggingExample"),
    path("IfTagDemo", views.ifTagDemo, name="ITGDEMO"),
    path("ShowProducts", views.ShowProducts, name="SP"),
    path("ShowUsers", views.LoadUsers, name="SU"),
    path("ShowUsers2", views.LoadUsers2, name="SU2"),
    path("ShowUserDetails", views.LoadUserDetails, name="ShowUserDetails"),
    path("PassModel", views.pass_model_2_template, name="PassModel"),
    path("BIFDemo", views.builtin_filters_demo, name="BIF"),
    path(
        "CustomFiltersDemo", views.custom_filters_demo, name="CustomFiltersDemo"  # noqa
    ),  # noqa
]
