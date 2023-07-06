from django.urls import path
from .views import FarmList, FarmDetail

urlpatterns = [
    path('', FarmList.as_view(), name = 'farm_list'),
    path('<int:pk>/', FarmDetail.as_view(), name = 'farm_detail'),
]

