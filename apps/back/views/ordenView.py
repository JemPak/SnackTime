from apps.back.models.orden import Orden
from apps.back.serializers.ordenSerializer import OrdenSerializer
from rest_framework import generics       

class OrdenListCreateView(generics.ListCreateAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class OrdenRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer