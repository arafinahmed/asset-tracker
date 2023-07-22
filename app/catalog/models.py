from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    company_id = models.ForeignKey(Company, to_field='id', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    company_id = models.ForeignKey(Company, to_field='id', on_delete=models.CASCADE)
    device_type = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.device_type} - {self.model} ({self.serial_number})"

class DeviceLog(models.Model):
    device_id = models.ForeignKey(Device, to_field='id', on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, to_field='id', on_delete=models.CASCADE)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    checkout_condition = models.TextField()
    return_condition = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.device_id} - {self.employee_id} ({self.checkout_date})"
