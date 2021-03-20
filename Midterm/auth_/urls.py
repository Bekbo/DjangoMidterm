from django.urls import path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from .views import UserRegisterView

urlpatterns = [
    path('login', obtain_jwt_token, name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
