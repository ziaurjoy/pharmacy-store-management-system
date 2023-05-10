from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    license_no = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_no= models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class CompanyBank(models.Model):
    bank_account_no = models.CharField(max_length=150)
    ifsc_no = models.CharField(max_length=100)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)


class CompanyAccount(models.Model):
    choices=(
        ("Debit","Debit"),
        ("Credit","Credit")
        )
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    transaction_type = models.CharField(choices=choices,max_length=25)
    transaction_amt = models.CharField(max_length=255)
    transaction_date = models.DateField(blank=True, null=True)
    payment_mode = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)



