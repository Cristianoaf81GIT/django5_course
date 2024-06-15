from typing import Any, Tuple, List
from django.db import models


# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=30)
    location_name = models.CharField(max_length=30)

    def __str__(self) -> Any:
        return self.dept_name


class Country(models.Model):
    country_name = models.CharField(max_length=30)

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
    country = models.CharField(max_length=100, choices=countries, default=None)
    email = models.EmailField(default="", max_length=100)
    phone_number = models.CharField(default="", max_length=20)
