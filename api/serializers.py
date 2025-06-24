from rest_framework import serializers
from .models import Candies

class CandiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candies
        fields = '__all__'