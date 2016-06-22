from rest_framework import generics

from .models import Aircraft
from .serializers import AircraftSerializer, AircraftDetailSerializer


class AircraftListView(generics.ListAPIView):
    serializer_class = AircraftSerializer
    queryset = Aircraft.objects.all()


class AircraftDetailView(generics.RetrieveAPIView):
    serializer_class = AircraftDetailSerializer
    queryset = Aircraft.objects.all()
