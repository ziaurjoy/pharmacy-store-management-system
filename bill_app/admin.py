from django.contrib import admin
from .models import Bill, BillDetails
# Register your models here.

admin.site.register(Bill)
admin.site.register(BillDetails)