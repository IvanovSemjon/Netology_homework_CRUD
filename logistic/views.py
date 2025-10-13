from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query)
            )
        return queryset


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def get_queryset(self):
        queryset = Stock.objects.all()

        # Поиск по ID продукта
        product_id = self.request.query_params.get('products')
        if product_id:
            queryset = queryset.filter(products__id=product_id)

        # Дополнительное задание: поиск по названию/описанию продукта
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(products__title__icontains=search_query) |
                Q(products__description__icontains=search_query)
            ).distinct()

        return queryset


@api_view(['GET'])
def simple_view(request):
    return Response({"message": "Hello, world!"})
