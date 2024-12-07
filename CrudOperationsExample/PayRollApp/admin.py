from django.contrib import admin

from .models import City, Employee, OnSiteEmployees, State

# Register your models here.

admin.site.register(Employee)
admin.site.register(OnSiteEmployees)
admin.site.register(State)
admin.site.register(City)
