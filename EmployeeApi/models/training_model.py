from django.db import models
from django.utils import timezone
from .employee_model import Employee

class Training(models.Model):
    employee_id = models.ForeignKey(Employee, related_name="employee", on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    date_created = timezone.now()

    def __str__(self):
        return f'{self.name} {self.date_created}'
