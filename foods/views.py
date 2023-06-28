from rest_framework import generics
from .serializers import FoodSerializer
from .models import Food

class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetail(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
