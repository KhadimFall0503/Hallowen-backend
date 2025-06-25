from rest_framework import serializers
from .models import Candies, Decorations

class CandiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candies
        fields = '__all__'


class DecorationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decorations
        fields = '__all__'