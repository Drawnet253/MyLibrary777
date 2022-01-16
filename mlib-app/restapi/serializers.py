from rest_framework import serializers
from core.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    '''Author Serializer needed because of relation to books'''
    class Meta:
        model = Author
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
    '''Books serializer'''
    authors = AuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'authors', 'isbn_13', 'cover_link',
                  'pages_count', 'publication_language', 'published_year')
