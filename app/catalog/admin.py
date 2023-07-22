from django.contrib import admin

from .models import Company, Device, DeviceLog, Employee


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'email')
    list_display = ('id', 'name', 'email')
    list_filter = ('name', 'email')
    ordering = ('name', 'email')
    readonly_fields = ('id',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'email', 'company_id')
    list_display = ('id', 'name', 'email', 'company_id')
    list_filter = ('name', 'email', 'company_id')
    ordering = ('name', 'email', 'company_id')
    readonly_fields = ('id',)

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    fields = ('id', 'device_type', 'model', 'serial_number', 'company_id')
    list_display = ('id', 'device_type', 'model', 'serial_number', 'company_id')
    list_filter = ('device_type', 'model', 'serial_number', 'company_id')
    ordering = ('device_type', 'model', 'serial_number', 'company_id')
    readonly_fields = ('id',)

@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
    fields = ('id', 'device_id', 'employee_id', 'checkout_date', 'return_date', 'checkout_condition', 'return_condition')
    list_display = ('id', 'device_id', 'employee_id', 'checkout_date', 'return_date', 'checkout_condition', 'return_condition')
    list_filter = ('device_id', 'employee_id', 'checkout_date', 'return_date', 'checkout_condition', 'return_condition')
    ordering = ('device_id', 'employee_id', 'checkout_date', 'return_date', 'checkout_condition', 'return_condition')
    readonly_fields = ('id',)