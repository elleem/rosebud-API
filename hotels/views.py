from rest_framework import generics
from .serializers import HotelSerializer
from .models import Hotel
from .permissions import IsOwnerOrReadOnly

class HotelList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    #authorization
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
