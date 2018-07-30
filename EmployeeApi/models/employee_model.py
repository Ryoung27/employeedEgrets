from django.db import models
from django.utils import timezone
from safedelete.models import SafeDeleteModel
from safedelete.models import NO_DELETE

class Employee(safeDeleteModel):
    _safedelete_policy = NO_DELETE
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length =50)
    date_created = timezone.now()
    department = models.CharField(max_length=50)
    supervisor = False

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

