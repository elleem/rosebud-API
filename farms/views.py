from rest_framework import generics
from .serializers import FarmSerializer
from .models import Farm
from .permissions import IsOwnerOrReadOnly

class FarmList(generics.ListCreateAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

class FarmDetail(generics.RetrieveUpdateDestroyAPIView):
    #authorization
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
