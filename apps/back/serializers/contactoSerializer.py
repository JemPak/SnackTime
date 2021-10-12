from django.db.models import fields
from rest_framework import serializers
from apps.back.models.contacto import Contacto

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['id_contacto','nombre','email','tel','comentario','asesoria']