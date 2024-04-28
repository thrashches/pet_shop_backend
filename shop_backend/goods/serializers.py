from rest_framework import serializers
from .models import Goods, ProductBasket, Characteristic, Category, Warehouse

class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ('name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class GoodsSerializer(serializers.ModelSerializer):
    characteristic = CharacteristicSerializer(many=True)
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    products = GoodsSerializer(many=True)
    class Meta:
        model = ProductBasket
        fields = '__all__'

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        basket = ProductBasket.objects.create(**validated_data)
        for product_data in products_data:
            product = product_data['product']
            warehouse_product = Warehouse.objects.get(product=product)
            warehouse_product.quantity -= product_data['quantity']
            warehouse_product.save()
            basket.products.add(product, through_defaults={'quantity': product_data['quantity']})
        return basket
