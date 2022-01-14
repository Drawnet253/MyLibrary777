from django.shortcuts import render
from core.models import Book, Author
from django.views.generic.list import ListView


class BooksListView(ListView):
    '''List all books in databese'''
    model = Book
    paginate_by = 6
    template_name = 'book/index.html'
    context_object_name = 'book_list'
