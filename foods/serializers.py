from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Food