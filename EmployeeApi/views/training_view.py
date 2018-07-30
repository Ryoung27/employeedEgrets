from rest_framework import viewsets
from Api import models
from Api import serializers


class Training_Viewset(viewsets.ModelViewSet):
    queryset = models.Training.objects.all()
    serializer_class = serializers.Training_Serializer