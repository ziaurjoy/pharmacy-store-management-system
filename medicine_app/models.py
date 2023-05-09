from django.db import models
from company_app.models import Company

# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length = 100)
    medical_typ = models.CharField(max_length = 100)
    buy_price = models.CharField(max_length = 100)
    sell_price = models.CharField(max_length = 100)
    c_gst = models.CharField(max_length = 100)
    s_gst = models.CharField(max_length = 100)
    batch_no = models.CharField(max_length = 100)
    shelf_no = models.CharField(max_length = 100)
    expire_date = models.DateField()
    mfg_date = models.DateField()
    company = models.ForeignKey(Company,on_delete = models.CASCADE)
    description = models.TextField()
    in_stock_total = models.IntegerField()
    qty_in_strip = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name



class MedicineDetails(models.Model):
    medicine = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    salt_name = models.CharField(max_length=100)
    salt_qty = models.CharField(max_length=100)
    salt_qty_type = models.CharField(max_length=100)
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.medicine.name
