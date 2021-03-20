from django.shortcuts import render
from rest_framework.decorators import action

from .models import User
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from .serializers import UserSerializer
# Create your views here.


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @action(methods=['POST'], detail=False, permission_classes=(AllowAny,))
    def register(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        user = User.objects.create_user(username=username, email=email, password=password)
        ser = UserSerializer(user)
        return Response(ser.data)

    def list(self, request, *args, **kwargs):
        ser = UserSerializer(self.queryset, many=True)
        print(ser.data)
        return Response(ser.data)

