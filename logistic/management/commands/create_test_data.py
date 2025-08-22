from django.core.management.base import BaseCommand
from logistic.models import Product, Stock, StockProduct


class Command(BaseCommand):
    help = 'Создает тестовые данные для продуктов и складов'

    def handle(self, *args, **options):
        # Создаем продукты
        products_data = [
            {'title': 'Помидоры', 'description': 'Свежие красные помидоры'},
            {'title': 'Огурцы', 'description': 'Хрустящие зеленые огурцы'},
            {'title': 'Картофель', 'description': 'Молодой картофель'},
            {'title': 'Морковь', 'description': 'Сладкая морковь'},
            {'title': 'Лук', 'description': 'Репчатый лук'},
        ]

        products = []
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                title=product_data['title'],
                defaults={'description': product_data['description']}
            )
            products.append(product)
            if created:
                self.stdout.write(f'Создан продукт: {product.title}')

        # Создаем склады
        stocks_data = [
            'Склад на Ленинградском шоссе',
            'Склад в Подмосковье',
            'Центральный склад',
        ]

        stocks = []
        for address in stocks_data:
            stock, created = Stock.objects.get_or_create(address=address)
            stocks.append(stock)
            if created:
                self.stdout.write(f'Создан склад: {stock.address}')

        # Добавляем продукты на склады
        import random
        from decimal import Decimal

        for stock in stocks:
            # Очищаем старые связи
            stock.positions.all().delete()
            
            # Добавляем случайные продукты на каждый склад
            selected_products = random.sample(products, random.randint(2, 4))
            
            for product in selected_products:
                StockProduct.objects.create(
                    stock=stock,
                    product=product,
                    quantity=random.randint(10, 100),
                    price=Decimal(str(random.uniform(50, 500))).quantize(Decimal('0.01'))
                )
                self.stdout.write(f'Добавлен {product.title} на {stock.address}')

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно созданы!'))