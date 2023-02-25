from django.urls import include, path
from rest_framework import routers

from .views import UsersViewSet, create_user, get_jwt_token

app_name = 'users'

router_v_1 = routers.DefaultRouter()
router_v_1.register('users', UsersViewSet, basename='users')

urlpatterns = [
    path('', include(router_v_1.urls)),
    path("auth/", include([
        path('signup/', create_user),
        path('token/', get_jwt_token)
    ])),
]
