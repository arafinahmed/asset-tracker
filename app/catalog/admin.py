from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    fields = ('id', 'name',)
    list_display = ('id', 'name',)
    list_filter = ('name', )
    ordering = ('name',)
    readonly_fields = ('id',)