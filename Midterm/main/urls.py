from django.urls import path
from .views import index
from rest_framework import routers
from .views import BooksViewSet, JournalViewSet
router = routers.SimpleRouter()
router.register('books', BooksViewSet, basename='books')
router.register('journals', JournalViewSet, basename='journals')

urlpatterns = [
]

urlpatterns += router.urls
