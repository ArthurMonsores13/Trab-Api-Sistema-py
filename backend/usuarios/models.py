from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=200)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
