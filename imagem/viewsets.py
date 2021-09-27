from rest_framework import viewsets
from . import models
from . import serializers


class ImagemViewSet (viewsets.ModelViewSet):
    queryset = models.Imagem.objects.all()
    serializer_class = serializers.ImagemSerializer


class AnaliseViewSet (viewsets.ModelViewSet):
    queryset = models.Analise.objects.all()
    serializer_class = serializers.AnaliseSerializer
