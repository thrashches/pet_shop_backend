from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

from goods.views import GoodViewSet
from authentication.views import EmailTokenObtainPairView, RegisterView

router = DefaultRouter()
router.register('goods', GoodViewSet, 'goods')

urlpatterns = [
    path('users/register/', RegisterView.as_view(), name='token_obtain_pair'),
    path('users/token/obtain/', EmailTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),

]
urlpatterns += router.urls
