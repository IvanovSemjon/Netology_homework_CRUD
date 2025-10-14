#!/usr/bin/env python
import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stocks_products.settings")
    django.setup()
    
    from django.urls import reverse
    from django.test import Client
    
    client = Client()
    
    # Проверяем доступные URL
    try:
        response = client.get('/api/v1/simple/')
        print(f"URL /api/v1/simple/ - Status: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}")
        else:
            print(f"Error: {response.content}")
    except Exception as e:
        print(f"Error accessing /api/v1/simple/: {e}")
    
    # Проверяем другие URL
    try:
        response = client.get('/api/v1/products/')
        print(f"URL /api/v1/products/ - Status: {response.status_code}")
    except Exception as e:
        print(f"Error accessing /api/v1/products/: {e}")