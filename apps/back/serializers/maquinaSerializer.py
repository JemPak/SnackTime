from django.db.models import fields
from rest_framework import serializers
from apps.back.models.maquina import Maquina
 
class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = ['id_maquina','id_propietario','id_ordenes_maquina','direc_maquina','is_activate']
    
    