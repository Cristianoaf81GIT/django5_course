from typing import Any, Tuple, List
from django.db import models


# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=255)
    location_name = models.CharField(max_length=255)

    def __str__(self) -> Any:
        return self.dept_name


class Country(models.Model):
    country_name = models.CharField(max_length=255)

    def __str__(self) -> Any:
        return self.country_name


class Employee(models.Model):
    countries: List[Tuple[str, str]] = [
        ("IND", "India"),
        ("BR", "Brazil"),
        ("UK", "United Kingdom"),
        ("AUS", "Australia"),
        ("USA", "United States"),
        ("AU", "Austria"),
        ("SP", "SPAIN"),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title_name = models.CharField(max_length=30)
    has_passport = models.BooleanField()
    salary = models.IntegerField()
    birth_date = models.DateField()
    hire_date = models.DateField()
    notes = models.CharField(max_length=200)
    # country = models.CharField(max_length=100, choices=countries, default=None)
    email = models.EmailField(default="", max_length=100)
    phone_number = models.CharField(default="", max_length=20)
    emp_department = models.ForeignKey(
        to="Department",  # can be model object itself or string if model is not defined yet
        default=0,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="Departments",
    )
    emp_country = models.ForeignKey(
        to="Country",
        default=0,
        on_delete=models.SET_NULL,
        related_name="Countries",
        null=True,
        blank=True,
    )


class PartTimeEmployee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title_name = models.CharField(max_length=30)

class State(models.Model):
    name = models.CharField(max_length=100, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, default=None)

    def __str__(self) -> str:
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100, null=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, default=None)

    def __str__(self) -> str:
        return self.name

class OnSiteEmployees(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=30, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, default=None)
    state = models.ForeignKey(State, on_delete=models.PROTECT, default=None)
    city = models.ForeignKey(City, on_delete=models.PROTECT, default=None)

    def __str__(self) -> str:
        return self.first_name


