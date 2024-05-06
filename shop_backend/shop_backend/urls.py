from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('shop_backend.v1_urls')),
    path('api/v1/', include('goods.v1_urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
