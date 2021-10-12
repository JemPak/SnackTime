from django.db.models import fields
from rest_framework import serializers
from apps.back.models.orden import Orden
 
class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = ['id_orden','fecha','id_productos','comentario']