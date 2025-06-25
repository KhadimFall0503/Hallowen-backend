from rest_framework import viewsets
from .models import Candies, Decorations
from .serializers import CandiesSerializer, DecorationsSerializer

class CandiesViewSet(viewsets.ModelViewSet):
    queryset = Candies.objects.all()
    serializer_class = CandiesSerializer

class DecorationsViewSet(viewsets.ModelViewSet):
    queryset = Decorations.objects.all()
    serializer_class = DecorationsSerializer
