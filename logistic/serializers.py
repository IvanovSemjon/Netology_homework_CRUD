from rest_framework import serializers
from logistic.models import Stock, Product, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description')


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ('product', 'quantity', 'price')


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ('id', 'address', 'positions')

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product_id=position['product'].id,
                defaults={
                    'quantity': position['quantity'], 
                    'price': position['price']
                }
            )
        return stock

    def update(self, instance, validated_data):
        positions_data = validated_data.pop('positions', [])

        instance.address = validated_data.get('address', instance.address)
        instance.save()

        instance.positions.all().delete()

        for position_data in positions_data:
            StockProduct.objects.create(
                stock=instance,
                product=position_data['product'],
                quantity=position_data['quantity'],
                price=position_data['price']
            )

        return instance
