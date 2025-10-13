from rest_framework.routers import DefaultRouter
from django.urls import path

from logistic.views import ProductViewSet, StockViewSet, simple_view

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = router.urls + [
    path('simple/', simple_view, name='simple_view'),
]
