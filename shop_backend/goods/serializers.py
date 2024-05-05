from rest_framework import serializers
from .models import Goods, Characteristic, Category

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