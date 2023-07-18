from django.db import models

# Create your models here.
class Pag_Contato(models.Model):
    nome = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    mensagem = models.TextField()
    objects = models.Manager()