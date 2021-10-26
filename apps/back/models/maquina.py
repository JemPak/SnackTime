from django.db import models
from .cliente import Cliente
from .orden import Orden

class Maquina (models.Model):
    id_maquina = models.AutoField(primary_key=True, blank=False)
    id_propietario=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_ordenes_maquina=models.ManyToManyField(Orden)
    direc_maquina=models.TextField(verbose_name="direccion maquina",max_length=80,null=True,blank=True)
    is_activate=models.BooleanField(verbose_name="maquina activa", default=False)

    def __str__(self):
        return self.id_propietario