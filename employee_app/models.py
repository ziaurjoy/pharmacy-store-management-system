from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    joining_date=models.DateField()
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    added_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    salary_date = models.DateField()
    salary_amount = models.CharField(max_length=15)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.name


class EmployeeBank(models.Model):
    bank_account_no = models.CharField(max_length=100)
    ifsc_no = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.name
