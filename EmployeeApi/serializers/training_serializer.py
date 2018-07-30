from rest_framework import serializers
from Api import models


class Training_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        'employee_id',
        'name',
        'date_created'
        )
        model = models.Training