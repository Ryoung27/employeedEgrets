from rest_framework import viewsets
from Api import models
from Api import serializers

class Computer_Viewset(viewsets.ModelViewSet):
    queryset = models.Computer.objects.all()
    serializer_class = serializers.Computer_Serializer
