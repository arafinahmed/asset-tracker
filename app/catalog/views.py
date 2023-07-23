from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer

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
    
class EmployeeDetail(APIView):
    def get(self, request, id):
        employees = Employee.objects.all().filter(company_id=id)
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

class EmployeeList(APIView):
    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceDetail(APIView):
    def get(self, request, id):
        devices = Device.objects.all().filter(company_id=id)
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

class DeviceList(APIView):
    def post(self, request, format=None):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceLogList(APIView):
    def post(self, request, format=None):
        serializer = DeviceLogSerializer(data=request.data)
        serializer2 = DeviceLogSerializer(data=request.data)

        if serializer2.is_valid() and serializer.is_valid():
            device_id = serializer.data["device_id"]
            employee_id = serializer.data["employee_id"]
            device = Device.objects.get(id=device_id)
            device_s = DeviceSerializer(device)
            employee = Employee.objects.get(id=employee_id)
            employee_s = EmployeeSerializer(employee)

            device_company = device_s.data["company_id"]
            employee_company = employee_s.data["company_id"]

            if device_company != employee_company:
                return Response("Device and Employee must be from the same company", status=status.HTTP_400_BAD_REQUEST)
            
            try:
                devicelog = DeviceLog.objects.all().filter(device_id=device_id).latest('id')
                devicelog_s = DeviceLogSerializer(devicelog)
                if devicelog_s.data["return_date"] == None:
                    return Response("Device is already checked out", status=status.HTTP_400_BAD_REQUEST)
                else:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                serializer2.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        serializer = DeviceLogSerializer(data=request.data)
        serializer2 = DeviceLogSerializer(data=request.data)

        if serializer.is_valid() and serializer2.is_valid():
            device_id = serializer.data["device_id"]
            employee_id = serializer.data["employee_id"]
            device = Device.objects.get(id=device_id)
            device_s = DeviceSerializer(device)
            employee = Employee.objects.get(id=employee_id)
            employee_s = EmployeeSerializer(employee)

            device_company = device_s.data["company_id"]
            employee_company = employee_s.data["company_id"]

            if device_company != employee_company:
                return Response({"message":"Device and Employee must be from the same company"}, status=status.HTTP_400_BAD_REQUEST)
            
            if serializer.data["return_date"] == None or serializer.data["return_condition"] == None:
                return Response({"message" : "Provide return date and return conditon"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                devicelog = DeviceLog.objects.all().filter(device_id=device_id).latest('id')
                devicelog_s = DeviceLogSerializer(devicelog)
                if devicelog_s.data["return_date"] == None:
                    update = DeviceLog.objects.get(id=devicelog_s.data["id"])
                    update.return_date = serializer.data["return_date"]
                    update.return_condition = serializer.data["return_condition"]
                    update.save()
                    return Response({"status":"Done"}, status=status.HTTP_200_OK)
                else:
                    return Response("Device is not checked out", status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response("Device is not checked out", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeviceLogDetail(APIView):
    def get(self, request, id):
        devicelogs = DeviceLog.objects.all().filter(device_id=id)
        serializer = DeviceLogSerializer(devicelogs, many=True)
        return Response(serializer.data)
