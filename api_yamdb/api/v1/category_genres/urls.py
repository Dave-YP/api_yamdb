from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, GenreViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')

urlpatterns = [
    path('', include(router_v1.urls)),
]
