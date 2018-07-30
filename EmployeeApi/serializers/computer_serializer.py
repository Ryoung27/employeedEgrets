from rest_framework import serializers
from Api import models


class Computer_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'department_id',
            'employee_id'
        )
        model = models.Computer