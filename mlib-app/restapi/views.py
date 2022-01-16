from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from core.models import Author, Book
from restapi.serializers import AuthorSerializer, BookSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet


class BookList(ListCreateAPIView):
    ''' List all books.'''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
