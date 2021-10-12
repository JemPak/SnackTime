from apps.back.models import Contacto
from apps.back.serializers import ContactoSerializer
from rest_framework import generics       

class ContactoListCreateView(generics.ListCreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

class ContactoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer