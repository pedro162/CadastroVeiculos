from django.db import models
from django.core.validators import MinValueValidator
from django.utils.datetime_safe import datetime

class Empresa(models.Model):
    nome_fantasia = models.CharField(null=False,max_length=255)
    cnpj = models.CharField(null=False, max_length=20)
    email = models.EmailField(null=False)

class Carro(models.Model):
    modelo  = models.CharField(max_length=50, null=False)
    marca   = models.CharField(max_length=50, null=False)
    ano     = models.PositiveIntegerField(validators=[MinValueValidator(2000)], null=False)
    valor   = models.FloatField(null=False)
    data_cadastro = models.DateTimeField(default=datetime.now(), null=False)
    #empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)