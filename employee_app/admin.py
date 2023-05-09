from django.contrib import admin
from .models import Employee, EmployeeBank, EmployeeSalary
# Register your models here.

admin.site.register(Employee)
admin.site.register(EmployeeBank)
admin.site.register(EmployeeSalary)