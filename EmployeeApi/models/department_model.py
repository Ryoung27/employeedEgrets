from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    duties = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.name}: {self.duties}'

