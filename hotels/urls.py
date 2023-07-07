from django.urls import path
from .views import HotelList, HotelDetail

urlpatterns = [
    path('', HotelList.as_view(), name = 'hotel_list'),
    path('<int:pk>/', HotelDetail.as_view(), name = 'hotel_detail'),
]

