from django.shortcuts import render


from medicine_app import models
from medicine_app import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class MedicineViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = models.Medicine.objects.all()
        serializer = serializers.MedicineQuerySerliazer(queryset, many=True)
        medicine_data = serializer.data
        new_medicine_list = []
        for medicine in medicine_data:
            medicine_details = models.MedicineDetails.objects.filter(medicine__id = medicine['id'])
            medicine_details_serializer = serializers.MedicineDetailsQuerySerliazer(medicine_details, many=True)
            medicine['medicine_details'] = medicine_details_serializer.data
            new_medicine_list.append(medicine)

        response_data = {
            "data": new_medicine_list,
            "message": "Response Success",
            "error": False,
            "status": status.HTTP_200_OK

        }
        return Response(response_data)


    def create(self, request):
        try:
            medicine_serializer = serializers.MedicineCreateSerliazer(data=request.data)
            medicine_serializer.is_valid(raise_exception=True)
            medicine_serializer.save()
            medicine_id = medicine_serializer.data['id']
            medicine_details_data = request.data['medicine_details']
            medicine_details_list = []
            for medicine_details in medicine_details_data:
                medicine_details['medicine'] = medicine_id
                medicine_details_list.append(medicine_details)
            medicine_details_serializer = serializers.MedicineDetailsCreateSerliazer(data=medicine_details_list, many=True)
            medicine_details_serializer.is_valid()
            medicine_details_serializer.save()

            response_data = {
                "message": "Medicine Data Save Successfully",
                "error": False,
                "status": status.HTTP_201_CREATED

            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Error Saving Medicine Data",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST

            }
            return Response(response_data)


    def retrieve(self, request, pk=None):
        medicine = models.Medicine.objects.get(id=pk)
        serializer = serializers.MedicineQuerySerliazer(medicine)
        medicine_data = serializer.data

        medicine_details = models.MedicineDetails.objects.filter(medicine__id = medicine_data['id'])
        medicine_details_serializer = serializers.MedicineDetailsQuerySerliazer(medicine_details, many=True)
        medicine_data['medicine_details'] = medicine_details_serializer.data
        response_data = {
            "data": medicine_data,
            "error": False,
            "status": status.HTTP_201_CREATED

        }
        return Response(response_data)



    def update(self, request, pk=None):
        
        try:
            queryset = models.Medicine.objects.get(id=pk)
            serializer = serializers.MedicineQuerySerliazer(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # print(request.data)
            response_data = {
                "data": serializer.data,
                "message": "Medicine Data Update Successfully",
                "error": False,
                "status": status.HTTP_201_CREATED
            }
            return Response(response_data)
        except Exception as err:
            print(err)
            response_data = {
                "message": "Error Update Medicine Data",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(response_data)


    def destroy(self, request, pk=None):
        try:
            medicine = models.Medicine.objects.get(id=pk)
            medicine.delete()
            response_data = {
                "message": "Medicine Data Delete Successfully",
                "error": False,
                "status": status.HTTP_202_ACCEPTED
            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Error Data Delete",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(response_data)






class MedicineDetailViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = models.MedicineDetails.objects.all()
        serializer = serializers.MedicineDetailsQuerySerliazer(queryset, many=True)
        response_data = {
            "data": serializer.data,
            "message": "Response Success",
            "error": False,
            "status": status.HTTP_200_OK

        }
        return Response(response_data)


    def create(self, request):
        try:
            serializer = serializers.MedicineDetailsCreateSerliazer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_data = {
                "data": serializer.data,
                "message": "MedicineDetail Data Save Successfully",
                "error": False,
                "status": status.HTTP_201_CREATED

            }
            return Response(response_data)
        except Exception as err:
            response_data = {
                "message": "Error Saving MedicineDetail Data",
                "error": err,
                "status": status.HTTP_400_BAD_REQUEST

            }
            return Response(response_data)


    def retrieve(self, request, pk=None):
        medicine_details = models.MedicineDetails.objects.get(id=pk)
        serializer = serializers.MedicineDetailsQuerySerliazer(medicine_details)
        return Response(serializer.data)


    def update(self, request, pk=None):
        try:
            queryset = models.MedicineDetails.objects.get(id=pk)
            serializer = serializers.MedicineDetailsQuerySerliazer(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_data = {
                "data": serializer.data,
                "message": "MedicineDetail Data Update Successfully",
                "error": False,
                "status": status.HTTP_201_CREATED
            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Error Update MedicineDetail Data",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(response_data)


    def destroy(self, request, pk=None):
        try:
            medicine_detail = models.MedicineDetails.objects.get(id=pk)
            medicine_detail.delete()
            response_data = {
                "message": "MedicineDetail Data Delete Successfully",
                "error": False,
                "status": status.HTTP_202_ACCEPTED
            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Error Data Delete",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(response_data)



