from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class CustomerRequest(models.Model):
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)
#     medicine_details=models.CharField(max_length=100)
#     status=models.BooleanField(default=False)
#     added_on=models.DateTimeField(auto_now_add=True)
#     prescription=models.FileField(default="")
