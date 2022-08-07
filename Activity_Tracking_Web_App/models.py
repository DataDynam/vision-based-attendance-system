from django.db import models
from datetime import datetime
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# Create your models here.


class Employee(models.Model):
    name = models.Char