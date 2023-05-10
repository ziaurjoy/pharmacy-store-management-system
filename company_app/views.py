
from company_app.models import Company
from company_app.serializers import CompanySerliazer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


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
        except:
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
        except:
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
        except:
            response_data = {
                "message": "Error Data Delete",
                "error": True,
                "status": status.HTTP_204_NO_CONTENT
            }
            return Response(response_data)


