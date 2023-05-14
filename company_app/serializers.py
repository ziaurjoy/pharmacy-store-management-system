
from rest_framework import serializers
from .models import Company, CompanyBank, CompanyAccount

class CompanySerliazer(serializers.ModelSerializer):
    class Meta:
        model=Company
        exclude = ('added_on',)


class CompanyBankSerliazer(serializers.ModelSerializer):
    class Meta:
        model=CompanyBank
        exclude = ('added_on',)
    
class CompanyBankSerliazerQuery(serializers.ModelSerializer):
    class Meta:
        model=CompanyBank
        fields = '__all__'
    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['company']=CompanySerliazer(instance.company).data
        return response


class CompanyAccountSerliazer(serializers.ModelSerializer):
    class Meta:
        model=CompanyAccount
        exclude = ('added_on',)


class CompanyAccountQuerySerliazer(serializers.ModelSerializer):
    class Meta:
        model=CompanyAccount
        exclude = ('added_on',)
        
    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['company']=CompanySerliazer(instance.company).data
        return response