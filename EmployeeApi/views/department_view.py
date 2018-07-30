from rest_framework import viewsets
from Api import models
from Api import serializers


class Department_Viewset(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.Department_Serializer