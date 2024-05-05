from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Goods
from .serializers import GoodsSerializer


class GoodsList(generics.ListCreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

class GoodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
