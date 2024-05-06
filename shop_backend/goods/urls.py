from rest_framework.routers import DefaultRouter

from .views import GoodViewSet

router = DefaultRouter()
router.register('goods', GoodViewSet, 'goods')
urlpatterns = router.urls
