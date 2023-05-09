from django.contrib import admin
from .models import Company, CompanyBank, CompanyAccount
# Register your models here.

admin.site.register(Company)
admin.site.register(CompanyBank)
admin.site.register(CompanyAccount)
