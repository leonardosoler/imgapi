from django.db.models.fields import DateTimeField
from rest_framework import serializers
from .models import Imagem, Analise
import datetime


class ImagemSerializer (serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = [
            'id_imagem',
            'nome_imagem',
            'tipo_imagem',
        ]


class AnaliseSerializer (serializers.ModelSerializer):
    class Meta:
        model = Analise
        fields = [
            'id_analise',
            'analise',
            'id_imagem',
            'tipo_analise',
            'data_cadastro',
            'data_modificacao',
            'status',
        ]
