from django.db import models

# Create your models here.


class Imagem (models.Model):
    id_imagem = models.AutoField(primary_key=True)
    nome_imagem = models.CharField(max_length=255)
    tipo_imagem = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_imagem


class Analise (models.Model):
    id_analise = models.AutoField(primary_key=True)
    analise = models.CharField(max_length=255)
    id_imagem = models.ForeignKey(
        'Imagem', on_delete=models.CASCADE, related_name='imagemof')
    tipo_analise = models.CharField(max_length=255)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.analise
