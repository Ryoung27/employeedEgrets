from django.db import models
from .employee_model import Employee
from django.utils import timezone
from .department_model import Department


class Computer(models.Model):
    name = models.CharField(max_length=50)
    employee_id = models.ForeignKey(Employee, related_name'employee', on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, related_name='department', on_delete=models.CASCADE)


