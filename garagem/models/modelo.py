from django.db import models
from garagem.models import Marca, Categoria

class Modelo(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.marca} {self.nome} {self.categoria}"
