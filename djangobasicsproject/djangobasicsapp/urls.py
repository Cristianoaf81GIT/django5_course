from django.urls import path, URLResolver, URLPattern
from . import views
from typing import Final

urlpatterns: Final[list[URLResolver | URLPattern]] = [
    path('', views.Home, name='entry'),
    path("Home", views.Home, name="Home"),
    path("ShowMessages", views.ShowMoreMessage, name="SM"),
    path("UseVariables", views.UseVariableAsResponse, name="UVR"),
    path("GetRequestDemo", views.GetRequestVariables, name="GRV"),
    path("ShowTime", views.ShowDateTimeInfo, name="SDTI"),
    path("LoggingDemo", views.LoggingExample, name="LoggingExample")
]
