from django.shortcuts import render
from core.models import Book, Author
from django.views.generic.list import ListView
from django.views.generic.base import View
from book.forms import CreateBookForm, ImportBooksForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from rest_framework import status
from django.shortcuts import redirect
import requests


class BooksListView(ListView):
    '''List all books in databese'''
    model = Book
    paginate_by = 6
    template_name = 'book/index.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        object_list = self.model.objects.all()
        book_title_input = self.request.GET.get('book_title')
        book_author_input = self.request.GET.get('book_author')
        book_language_input = self.request.GET.get('language')
        book_from_date_input = self.request.GET.get('from_date')
        book_to_date_input = self.request.GET.get('to_date')

        if book_title_input:
            object_list = object_list.filter(title__icontains=book_title_input)

        if book_author_input:
            authors_query = Author.objects.filter(
                name__icontains=book_author_input
            )
            authors_list = [x.id for x in authors_query]
            object_list = object_list.filter(authors__in=authors_list)

        if book_language_input:
            object_list = object_list.filter(
                publication_language__icontains=book_language_input
            )

        if book_from_date_input and not book_to_date_input:
            object_list = object_list.filter(
                published_year__gte=book_from_date_input)
        elif book_to_date_input and not book_from_date_input:
            object_list = object_list.filter(
                published_year__lte=book_to_date_input)
        elif book_from_date_input and book_to_date_input:
            object_list = object_list.filter(
                published_year__gte=book_from_date_input,
                published_year__lte=book_to_date_input
            )

        return object_list


class CreateBookView(CreateView):
    '''View for adding a book'''
    model = Book
    form_class = CreateBookForm
    template_name = 'book/add_book.html'
    success_url = reverse_lazy('index')


class BooksImportView(View):
    ''''View for import books from google api'''
    form_class = ImportBooksForm
    template_name = 'book/import.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


def books_import(request):
    params_dict = {
        'q': request.GET.get('keywords', False),
        'intitle': request.GET.get('intitle', False),
        'inauthor': request.GET.get('inauthor', False),
        'inpublisher': request.GET.get('inpublisher', False),
        'subject': request.GET.get('subject', False),
        'isbn': request.GET.get('isbn', False),
        'lccn': request.GET.get('lccn', False),
        'oclc': request.GET.get('oclc', False)
    }
    true_count = 0
    for param in params_dict.values():
        if param:
            true_count += 1

    if true_count == 0:
        return redirect('/import')

    # Remove empty items
    params_dict = {k: v for k, v in params_dict.items() if v}

    url = 'https://www.googleapis.com/books/v1/volumes'
    response = requests.get(url, params=params_dict)

    if response.status_code != status.HTTP_200_OK:
        return render(request,
                      'book/index.html',
                      {'message': 'Problem with service Google Books.'})

    json_data = response.json()

    if 'items' not in json_data:
        return render(request,
                      'book/index.html',
                      {'message': 'There were no books for such keywords.'})
    searched_books = json_data['items']

    for book in searched_books:
        if 'authors' in book['volumeInfo']:  # authors can be not provided
            authors = []
            for author in book['volumeInfo']['authors']:
                authors.append(Author.objects.create(name=author))
        else:
            authors = Author.objects.filter(name='Author Not provided')
            if len(authors) == 0:
                authors = [Author.objects.create(name='Author Not provided')]

        if 'pageCount' in book['volumeInfo']:
            pages_count = book['volumeInfo']['pageCount']
        else:
            pages_count = 0
        ind_ids = book['volumeInfo']['industryIdentifiers']
        isbn_13 = 0
        for ind_id in ind_ids:  # isbn_13 can be missing
            if 'ISBN_13' in ind_id.values():
                isbn_13 = ind_id['identifier']
        cover_link = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Book_%2889362%29_-_The_Noun_Project.svg/1024px-Book_%2889362%29_-_The_Noun_Project.svg.png'
        if 'imageLinks' in book['volumeInfo']:  # imagelinks may be missing to
            if 'thumbnail' in book['volumeInfo']['imageLinks']:
                cover_link = book['volumeInfo']['imageLinks']['thumbnail']

        book, created = Book.objects.get_or_create(
            title=book['volumeInfo']['title'],
            published_year=book['volumeInfo']['publishedDate'][:4],
            pages_count=pages_count,
            publication_language=book['volumeInfo']['language'],
            cover_link=cover_link,
            isbn_13=isbn_13
            )
        if not created:
            book.authors.set(authors)
            book.save()
        book.authors.set(authors)
    return HttpResponseRedirect(reverse('index'))
