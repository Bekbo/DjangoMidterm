from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book, Journal
from auth_.models import User
from auth_.serializers import UserSerializer
# Create your views here.
from .serializers import BookSerializer, JournalSerializer


def index(request):
    return render(request, template_name='index.html', context={})


class BooksViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminUser,)

    def list(self, request, *args, **kwargs):
        ser = BookSerializer(self.queryset, many=True)
        return Response(ser.data)


class JournalViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = (IsAdminUser,)

    def list(self, request, *args, **kwargs):
        ser = JournalSerializer(self.queryset, many=True)
        return Response(ser.data)


