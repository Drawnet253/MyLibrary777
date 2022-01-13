from django.test import TestCase
from core import models


class ModelTests(TestCase):

    def test_author_str(self):
        '''Test the author string representation'''
        author = models.Author.objects.create(name='Adam Mickiewicz')
        self.assertEqual(str(author), author.name)

    def test_book_str(self):
        '''Test the book string representation'''
        book = models.Book.objects.create(
            title='Krew elfów, Tom 2',
            cover_link='',
            isbn_13='9788370540791',
            liczba_stron=295,
            publication_language='pl'
        )
        self.assertEqual(str(book), book.title)
