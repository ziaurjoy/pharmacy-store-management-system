from django.db import models
from customer_app.models import Customer
from medicine_app.models import Medicine

# # Create your models here.

class Bill(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)


class BillDetails(models.Model):
    bill = models.ForeignKey(Bill,on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    qty = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)
