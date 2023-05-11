from django.shortcuts import render, redirect
from .forms import DepartmentForm, EmployeeForm
from .models import Department, Employee
import csv
import json
from django.http import HttpResponse


def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_create')
    else:
        departments = Department.objects.all()
        form = DepartmentForm()
    return render(request, 'department_create.html', {'form': form,'departments': departments})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_create')
    else:
        employees = Employee.objects.all()
        form = EmployeeForm()
    return render(request, 'employee_create.html', {'form': form,'employees': employees})





def export_employee_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employee_data.csv"'

    writer = csv.writer(response)

    employees = Employee.objects.all()
    for employee in employees:
        department_dict = {str(dep.id): dep.name for dep in employee.departments.all()}
        department_json = json.dumps(department_dict)
        writer.writerow([employee.id, employee.name, department_json])

    return response
