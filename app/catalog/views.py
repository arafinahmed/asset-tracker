from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer

from django.http import HttpResponse

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
def sya_hello(request):
    return HttpResponse("Hello World!")

class CompanyList(APIView):
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeList(APIView):
    def get(self, request, id):
        employees = Employee.objects.all().filter(company_id=id)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

class EmployeeDetail(APIView):
    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)