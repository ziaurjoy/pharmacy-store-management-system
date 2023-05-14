
from rest_framework import serializers
from .models import Medicine, MedicineDetails



class MedicineCreateSerliazer(serializers.ModelSerializer):
    class Meta:
        model=Medicine
        exclude = ('added_on',)


class MedicineQuerySerliazer(serializers.ModelSerializer):
    class Meta:
        model=Medicine
        fields = '__all__'





class MedicineDetailsCreateSerliazer(serializers.ModelSerializer):
    class Meta:
        model=MedicineDetails
        exclude = ('added_on',)


class MedicineDetailsQuerySerliazer(serializers.ModelSerializer):
    class Meta:
        model=MedicineDetails
        fields = '__all__'

    # def to_representation(self, instance):
    #     response=super().to_representation(instance)
    #     response['medicine']=MedicineQuerySerliazer(instance.medicine).data
    #     return response

