from rest_framework import generics
from .serializers import FarmSerializer
from .models import Farm

class FoodList(generics.ListCreateAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
