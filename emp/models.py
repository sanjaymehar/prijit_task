from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    departments = models.ManyToManyField(Department)

    def __str__(self):
        return self.name
