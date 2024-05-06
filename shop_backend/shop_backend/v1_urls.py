from django.urls import path, include

urlpatterns = [
    path('users/', include('authentication.urls')),

]
