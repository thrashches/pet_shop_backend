from rest_framework import serializers

from .models import Goods, Category, Characteristic


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class GoodsSerializer(serializers.ModelSerializer):
    characteristic = CharacteristicSerializer(many=True,)
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'
