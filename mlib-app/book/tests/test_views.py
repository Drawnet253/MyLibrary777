from django.test import TestCase, Client
from rest_framework import status
from core.models import Book, Author


class BooksListViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_books_list_view(self):
        '''Test that /book/ url is working'''
        res = self.client.get('/book/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
