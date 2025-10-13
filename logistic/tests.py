from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from logistic.models import Product, Stock


class ProductAPITest(APITestCase):
    def test_create_product(self):
        data = {'title': 'Test Product', 'description': 'Test Description'}
        response = self.client.post('/api/v1/products/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_get_products(self):
        Product.objects.create(title='Test Product')
        response = self.client.get('/api/v1/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class StockAPITest(APITestCase):
    def test_create_stock(self):
        product = Product.objects.create(title='Test Product')
        data = {
            'address': 'Test Address',
            'positions': [{'product': product.id, 'quantity': 10, 'price': '100.00'}]
        }
        response = self.client.post('/api/v1/stocks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Stock.objects.count(), 1)

    def test_get_stocks(self):
        Stock.objects.create(address='Test Address')
        response = self.client.get('/api/v1/stocks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SimpleViewTest(APITestCase):
    def test_simple_view(self):
        response = self.client.get('/api/v1/simple/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Hello, world!')