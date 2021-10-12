from django.db.models import fields
from rest_framework import serializers
from apps.back.models.producto import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_producto','nombre','cantidad','precio','descripcion']