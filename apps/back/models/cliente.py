from django.db import models

# Create your models here.
class Cliente (models.Model):
    id_cliente = models.AutoField(verbose_name="id cliente",primary_key=True, null=False)
    nombre = models.CharField(verbose_name="nombre",max_length=50, null=False, blank=False)
    nit = models.IntegerField(verbose_name="identificacion",null=False, blank=False)
    direc = models.CharField(verbose_name="direccion", max_length= 200,null=True, blank=True)
    ciudad = models.CharField(verbose_name="ciudad",max_length=80, blank=False)
    email = models.EmailField(null=False, blank=False)
    tel = models.IntegerField(verbose_name="telefono",null=False, blank=False)

    def __str__(self):
        return self.nombre