from django.db.models import fields
from rest_framework import serializers
from apps.back.models.cliente import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id_cliente','nombre','nit','direc','ciudad','email','tel']