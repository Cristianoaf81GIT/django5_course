from typing import Final
from django.urls import path, URLPattern, URLResolver
from . import views

urlpatterns: Final[list[URLResolver | URLPattern]] = [
    path("", views.Home, name="root"),
    path("Home", views.Home, name="Home")
]
