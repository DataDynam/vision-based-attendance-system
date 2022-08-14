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
    arrival_time = models.Ch