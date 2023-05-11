from django.contrib import admin
from django.urls import path
from emp.views import (
    department_create,
    employee_create,
    export_employee_data,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('department/create/', department_create, name='department_create'),
    path('employee/create/', employee_create, name='employee_create'),
    path('employee/export/', export_employee_data, name='export_employee_data'),
]
