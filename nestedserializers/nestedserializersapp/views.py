from nestedserializersapp.models import (Autor, Books)
from nestedserializersapp.serializers import (AuthorSerializer, BookSerializers)
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

# ! pagination class below 
class BookPagination(PageNumberPagination):
    page_size = 5

class AuthorListView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AuthorSerializer
   

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AuthorSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializers
    pagination_class = LimitOffsetPagination

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializers