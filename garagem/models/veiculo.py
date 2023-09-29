from django.db import models
from garagem.models import  Modelo, Cor, Acessorio
from uploader.models import Image

class Veiculo(models.Model):
    imagem = models.ManyToManyField(
        Image,
        related_name="+",
        blank=True,
        default=None,
    )
    acessorio = models.ManyToManyField(Acessorio)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    descricao = models.CharField(null=True,blank=True,max_length=100)
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")

    def __str__(self):
        return f"  {self.modelo} {self.ano} {self.cor}"
