from django.db import models
from .producto import Producto 

class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    id_productos = models.ManyToManyField(Producto)
    comentario = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.id_orden