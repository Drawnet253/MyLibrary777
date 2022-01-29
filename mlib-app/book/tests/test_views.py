from django.test import TestCase, Client
from rest_framework import status
from core.models import Book, Author
from core.validators import is_isbn13


BOOKS_URL = '/book/'
NEW_URL = '/book/new'


def sample_book(**params):
    '''Create and return sample book'''
    author = Author(name='Jan Nowak')
    author.save()

    defaults = {
        'title': 'Sample title of the book',
        'pages_count': 1,
        'publication_language': 'US',
        'isbn_13': '9788364863011'
    }
    defaults.update(params)
    book = Book.objects.create(**defaults)
    book.authors.add(author)
    book.save()
    return book


class BooksListViewTest(TestCase):
    '''Public tests for book list view'''
    def setUp(self):
        self.client = Client()

    def test_books_list_view(self):
        '''Test that /book/ url is working'''
        res = self.client.get(BOOKS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_isbn13_validation(self):
        '''Test if database creates only valid ISBN13 numbers'''
        bad_isbn13 = '9781734314509'

        self.assertFalse(is_isbn13(bad_isbn13))

    def test_filter_title(self):
        '''Test that filtering books by title is working'''
        keyword = 'Learning of programming in python'
        book1 = sample_book(title=keyword)
        book2 = sample_book(title='Learning' + keyword)
        book3 = sample_book(title='Third book')

        res = self.client.get(BOOKS_URL, {'title': 'programming'})

        self.assertIsNotNone(res.context)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        print('>>> START:'+str(res.context['book_list'])+'END')

        queryset = Book.objects.filter(title__icontains='programming')
        print('>>> FILTER:'+str(queryset)+'END')
        self.assertQuerysetEqual(res.context['book_list'], queryset, ordered=False)
        self.assertEqual(len(res.context['book_list']), 2)
