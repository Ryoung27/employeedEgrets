from rest_framework import serializers
from Api import models

class Employee_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'date_created',
            'department',
            'supervisor'
        )
        model = models.Employee