from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Goods
from .serializers import GoodsSerializer


class GoodViewSet(viewsets.ViewSet):
    queryset = Goods.objects.all()

    def list(self, request):
        serializer = GoodsSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(Goods, pk=pk)
        serializer = GoodsSerializer(product)
        return Response(serializer.data)

    def create(self, request):
        serializer = GoodsSerializer(self.request.data)
        return Response(serializer.data)
