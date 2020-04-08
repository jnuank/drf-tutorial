from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from shop.admin import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    本モデルのCRUD用API(ViewがAPIとなる)
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

