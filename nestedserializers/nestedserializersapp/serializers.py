from nestedserializersapp.models import (Autor, Books)
from rest_framework import serializers

# NOTE:- in this we hav kept the Authors below so that it can use Boook serializer

class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializers(read_only=True, many=True) #! here is where we tell our autor serializer to give all the values of books written by that 
    #! author to serialize also so that we can get the books when looking for author info.
    class Meta:
        model = Autor
        fields = '__all__'