from django.db import models

# Create your models here.
tipos_asesorias=(
        ('Informacion','Informacion'),
        ('Instalacion','Instalacion'),
        ('Quejas y reclamos','Quejas y reclamos')
 )

class Contacto (models.Model):
    
    id_contacto = models.AutoField(verbose_name="id cliente",primary_key=True, null=False)
    nombre = models.CharField(verbose_name="nombre",max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    tel = models.IntegerField(verbose_name="telefono",null=False, blank=False)
    asesoria=models.CharField(max_length=50, choices=tipos_asesorias, null=False, blank=False, verbose_name="asesoria")
    comentario= models.TextField(max_length=600, null=True, blank=True)