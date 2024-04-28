from rest_framework import generics, permissions

from .models import Goods, ProductBasket
from .serializers import GoodsSerializer, BasketSerializer

class GoodsList(generics.ListCreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

class GoodsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class ProduckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductBasket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [permissions.IsAuthenticated]

