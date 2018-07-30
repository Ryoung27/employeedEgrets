from rest_framework import serializers
from Api import models


class Department_Serializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'duties'
        )
        model = models.Department