from django.contrib import admin
from .models import *

@admin.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email_address','phone_number')
    search_fields = ('first_name','last_name','email_address')
    list_per_page = 10