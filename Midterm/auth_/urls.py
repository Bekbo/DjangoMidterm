from django.urls import path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from .views import UserViewSet
router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('login', obtain_jwt_token, name='index'),
]
urlpatterns += router.urls
