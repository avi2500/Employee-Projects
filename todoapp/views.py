from django.shortcuts import render,get_object_or_404
from todoapp.models import *


def index(request):
    emp = Employee.objects.all()
    context = {
        'employees':emp,
    }
    return render(request, 'index.html', context)

def employee_detail(request,pk):
    
    employee = get_object_or_404(Employee,pk=pk)
    
    context = {
        'employee':employee,
    }
    return render(request, 'employee_detail.html', context)

