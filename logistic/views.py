from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class Pagination(PageNumberPagination):
    page_size = 15


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_set_fields = ['id', 'title', 'description']
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'title', 'description']
    pagination_class = Pagination


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filterset_fields = ['address', ]
    search_fields = ['address',
                     '=positions__product__id',
                     'positions__product__title',
                     'positions__product__description']
    ordering_fields = ['id', 'address']

    pagination_class = Pagination
