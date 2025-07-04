from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from .models import Candies, Decorations
from .serializers import CandiesSerializer, DecorationsSerializer

# FilterSet pour Candies
class CandiesFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Candies
        fields = ['name', 'description']

# FilterSet pour Decorations
class DecorationsFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Decorations
        fields = ['name', 'description']

# ViewSet Candies avec filtrage
class CandiesViewSet(viewsets.ModelViewSet):
    queryset = Candies.objects.all()
    serializer_class = CandiesSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CandiesFilter
    search_fields = ['name', 'description']

# ViewSet Decorations avec filtrage
class DecorationsViewSet(viewsets.ModelViewSet):
    queryset = Decorations.objects.all()
    serializer_class = DecorationsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = DecorationsFilter
    search_fields = ['name', 'description']
