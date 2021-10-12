from apps.back.models.maquina import Maquina
from apps.back.serializers.maquinaSerializer import MaquinaSerializer
from rest_framework import generics       

class MaquinaListCreateView(generics.ListCreateAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer

class MaquinaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer