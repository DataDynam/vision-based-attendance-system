from django.db import models
from datetime import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Activity(models.Model):
    Employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    date = models.DateField(default=datetime.now)
    arrival_time = models.CharField(max_length=10000, blank=True, null=True)
    depart_time = models.CharField(max_length=10000, blank=True, null=True)
    on_working = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    off_working = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    fun_area_time = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    active = models.BooleanField(default=True)
    exception = models.BooleanField(default=False)
    comment = models.CharField(max_length=10000, blank=True, null=True)

    def Employee_name(self):
        return Employee.name


def content_file_name(instance, filename):
    filename, ext = filename.split('.')
    file_path = 'photos/' + '{name}/user_{user_id}.{filename}.