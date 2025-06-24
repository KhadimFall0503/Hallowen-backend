from django.shortcuts import render
from rest_framework import viewsets
from .models import Candies
from .serializers import CandiesSerializer

# Create your views here.
class CandiesViewSet(viewsets.ModelViewSet):
    queryset = Candies.objects.all()
    serializer_class = CandiesSerializer

    def get_queryset(self):
        queryset = Candies.objects.all()
        serializer_class = CandiesSerializer
        return queryset
