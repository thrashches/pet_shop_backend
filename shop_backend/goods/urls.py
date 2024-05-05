from django.urls import path

from .views import GoodsList, GoodsDetail


urlpatterns = [
    path('goods/', GoodsList.as_view()),
    path('goods/<pk>/', GoodsDetail.as_view()),
]
