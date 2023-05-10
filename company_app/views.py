
from company_app.models import Company, CompanyBank, CompanyAccount
from company_app.serializers import CompanySerliazer, CompanyBankSerliazer, CompanyBankSerliazerQuery, CompanyAccountSerliazer, CompanyAccountQuerySerliazer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

import datetime



# Create your views here.


class CompanyViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerliazer(queryset, many=True)
        response_data = {
            "data": serializer.data,
            "message": "Response Success",
            "error": False,
            "status": status.HTTP_200_OK

        }
        return Response(response_data)


    def create(self, request):
        try:
            serializer = CompanySerliazer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_data = {
                "data": serializer.data,
                "message": "Company Data Save Successfully",
                "error": False,
                "status": status.HTTP_201_CREATED

            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Error Saving Company Data",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST

            }
            return Response(response_data)


    def retrieve(self, request, pk=None):
        company = Company.objects.get(id=pk)
        serializer = CompanySerliazer(company)
        return Response(serializer.data)


    def update(self, request, pk=None):
        try:
            queryset = Company.objects.get(id=pk)
            serializer = CompanySerliazer(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_data = {
                "data": serializer.data,
                "message": "Company Data Update Successfully",
                "error": False,
                "status": status.HTTP_201_CREATED
            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Error Update Company Data",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(response_data)


    def destroy(self, request, pk=None):
        try:
            company = Company.objects.get(id=pk)
            company.delete()
            response_data = {
                "message": "Company Data Delete Successfully",
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





class CompanyBankViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = CompanyBank.objects.all()
        serializer = CompanyBankSerliazerQuery(queryset, many=True)
        response_data = {
            "data": serializer.data,
            "message": "Response Company Bank Data Success",
            "error": False,
            "status": status.HTTP_200_OK

        }
        return Response(response_data)


    def create(self, request):
        try:
            serializer = CompanyBankSerliazer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_data = {
                "data": serializer.data,
                "message": "Company Bank Data Save Successfully",
                "error": False,
                "status": status.HTTP_201_CREATED

            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Error Saving Company Bank Data",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST

            }
            return Response(response_data)


    def retrieve(self, request, pk=None):
        try:
            company_bank = CompanyBank.objects.get(id=pk)
            serializer = CompanyBankSerliazerQuery(company_bank)
            response_data = {
                "data": serializer.data,
                "message": "Company Bank Data",
                "error": False,
                "status": status.HTTP_200_OK

            }
            return Response(response_data)
        
        except Exception:
            company_bank = CompanyBank.objects.get(id=pk)
            serializer = CompanyBankSerliazerQuery(company_bank)
            response_data = {
                "message": "Error Company Bank Data",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST

            }
            return Response(response_data)


    def update(self, request, pk=None):
        try:
            queryset = CompanyBank.objects.get(id=pk)
            serializer = CompanyBankSerliazer(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_data = {
                "data": serializer.data,
                "message": "Company Bank Data Update Successfully",
                "error": False,
                "status": status.HTTP_201_CREATED
            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Error Update Company Bank Data",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(response_data)


    def destroy(self, request, pk=None):
        try:
            company_bank = CompanyBank.objects.get(id=pk)
            company_bank.delete()
            response_data = {
                "message": "Company Bank Data Delete Successfully",
                "error": False,
                "status": status.HTTP_202_ACCEPTED
            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Error Company Bank Data Delete",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(response_data)
        



class CompanyAccounViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = CompanyAccount.objects.all()
        serializer = CompanyAccountQuerySerliazer(queryset, many=True)
        response_data = {
            "data": serializer.data,
            "message": "Response Company Account Data Success",
            "error": False,
            "status": status.HTTP_200_OK

        }
        return Response(response_data)

    def create(self, request):
        
        try:
            serializer = CompanyAccountSerliazer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_data = {
                "data": serializer.data,
                "message": "Company Account Data Save Successfully",
                "error": False,
                "status": status.HTTP_201_CREATED

            }
            return Response(response_data)
        except Exception as err:
            print(err)
            response_data = {
                "message": "Error Saving Company Account Data",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST

            }
            return Response(response_data)


    def retrieve(self, request, pk=None):
        try:
            company_account = CompanyAccount.objects.get(id=pk)
            serializer = CompanyAccountQuerySerliazer(company_account)
            response_data = {
                "data": serializer.data,
                "message": "Company Account Data",
                "error": False,
                "status": status.HTTP_200_OK

            }
            return Response(response_data)
        
        except Exception:
            response_data = {
                "message": "Error Company Account Data",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST

            }
            return Response(response_data)


    def update(self, request, pk=None):
        try:
            queryset = CompanyAccount.objects.get(id=pk)
            serializer = CompanyAccountSerliazer(queryset, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_data = {
                "data": serializer.data,
                "message": "Company Account Data Update Successfully",
                "error": False,
                "status": status.HTTP_201_CREATED
            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Error Update Company Account Data",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(response_data)


    def destroy(self, request, pk=None):
        try:
            company_account = CompanyAccount.objects.get(id=pk)
            company_account.delete()
            response_data = {
                "message": "Company Account Delete Successfully",
                "error": False,
                "status": status.HTTP_202_ACCEPTED
            }
            return Response(response_data)
        except Exception:
            response_data = {
                "message": "Error Company Account Data Delete",
                "error": True,
                "status": status.HTTP_400_BAD_REQUEST
            }
            return Response(response_data)