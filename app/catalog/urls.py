from django.urls import path
from . import views

from . import views

urlpatterns = [
    path("alive/", views.sya_hello),
    
    path("companies/", views.CompanyList.as_view()),
    path("employees/", views.EmployeeList.as_view()),
    path("devices/", views.DeviceList.as_view()),
    path("logs/", views.DeviceLogList.as_view()),

    path("employees/<int:id>", views.EmployeeDetail.as_view()),
    path("devices/<int:id>", views.DeviceDetail.as_view()),
    path("logs/<int:id>", views.DeviceLogDetail.as_view()),
]