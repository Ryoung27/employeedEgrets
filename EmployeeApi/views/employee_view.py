from rest_framework import viewsets
from Api import models
from Api import serializers



class Employee_Viewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.Employee_Serializer