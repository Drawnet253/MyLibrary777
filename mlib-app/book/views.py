
from core.models import Book, Author
from django.views.generic.list import ListView
from book.forms import CreateBookForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


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
