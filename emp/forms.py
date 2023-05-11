from django import forms
from .models import Department, Employee


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']


class EmployeeForm(forms.ModelForm):
    departments = forms.ModelMultipleChoiceField(queryset=Department.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Employee
        fields = ['name', 'age', 'departments']
