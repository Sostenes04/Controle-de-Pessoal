from operator import mod
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

# Create your models here.

class Registar(models.Model):

    Bairro = models.CharField(max_length=50)
    Primeiro_Nome = models.CharField(max_length=255)
    Apelido = models.CharField(max_length=255)
    telemovel = models.IntegerField()
    ID_cadastro = models.CharField(max_length=12)
    latitude = models.FloatField()
    longitude = models.FloatField()
    autor = models.ForeignKey(User,
    on_delete=models.PROTECT)
    

    def __str__(self):
        return self.Bairro
    

