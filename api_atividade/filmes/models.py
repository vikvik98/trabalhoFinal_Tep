from django.db import models
from django.conf import settings

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=200, blank=True, default="")

class Filme(models.Model):
    usuario = models.ForeignKey(
        'auth.User',
        related_name='filmes',
        on_delete= models.CASCADE
    )
    nome = models.CharField(max_length=200, blank=True, default="")
    categoria = models.ForeignKey(Categoria, related_name="filmes", on_delete=models.CASCADE)




