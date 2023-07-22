from django.urls import path
from . import views

from . import views

urlpatterns = [
    path("alive/", views.sya_hello),
    path("companies/", views.CompanyList.as_view()),
]