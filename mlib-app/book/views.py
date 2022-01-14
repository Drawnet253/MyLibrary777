from django.shortcuts import render
from core.models import Book, Author
from django.views.generic.list import ListView


class BooksListView(ListView):
    model = Book
    paginate_by = 10
    template_name = 'book/index.html'
    context_object_name = 'book_list'
