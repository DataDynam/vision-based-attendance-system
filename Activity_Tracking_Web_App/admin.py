
# Register your models here.
from django.contrib import admin
from django.apps import apps
# Register your models here.
from .models import Employee, Picture, Activity


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name']
    pass


class ActivityAdmin(admin.ModelAdmin):

    list_display = ['Employee', 'date', 'arrival_time', 'depart_time', 'on_working