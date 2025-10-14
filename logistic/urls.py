from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view

from logistic.views import ProductViewSet, StockViewSet, simple_view

@api_view(['GET'])
def api_root(request):
    return Response({
        'products': request.build_absolute_uri('products/'),
        'stocks': request.build_absolute_uri('stocks/'),
        'simple': request.build_absolute_uri('simple/'),
    })

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [
    path('', api_root, name='api_root'),
] + router.urls + [
    path('simple/', simple_view, name='simple_view'),
]
