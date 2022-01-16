from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from core.models import Book, Author
from restapi.serializers import BookSerializer, AuthorSerializer
from restapi.views import BookList, FilteredBookList


ALL_BOOKS_URL = reverse('restapi:book-list')
FILTER_BOOKS_URL = reverse('restapi:filter-list')


class PublicBookApiTests(TestCase):
    '''Test unauthenticated recipe API access'''

    def setUp(self):
        self.client = APIClient()

    def test_auth_not_required(self):
            """Test the authenticaiton is not required"""
            res = self.client.get(ALL_BOOKS_URL)
            self.assertEqual(res.status_code, status.HTTP_200_OK)

            res = self.client.get(FILTER_BOOKS_URL)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
