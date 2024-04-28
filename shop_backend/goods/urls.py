from django.urls import path

from .views import GoodsList, GoodsDetail, ProduckDetail

urlpatterns = [
    path('goods/', GoodsList.as_view()),
    path('goods/<pk>/', GoodsDetail.as_view()),
    path('basket/<pk>/', ProduckDetail.as_view()),
]