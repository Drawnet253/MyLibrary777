from core.models import Author, Book
from restapi.serializers import BookSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView


class BookList(ListCreateAPIView):
    ''' List all books with posibility to add new one.'''
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class FilteredBookList(ListAPIView):
    '''List of books, can be filtered by 5 parameters.GET.'''
    serializer_class = BookSerializer

    def get_queryset(self):
        '''filtered queryset using query parameters from the URL.'''

        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        language = self.request.query_params.get('lang')
        pub_start = self.request.query_params.get('pub_start')
        pub_end = self.request.query_params.get('pub_end')
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        if author is not None:
            authors_query = Author.objects.filter(
                    name__icontains=author)
            authors_list = [x.id for x in authors_query]
            queryset = queryset.filter(authors__in=authors_list)
        if language is not None:
            queryset = queryset.filter(
                publication_language__icontains=language)
        if pub_start and not pub_end:
            queryset = queryset.filter(
                published_year__gte=pub_start)
        elif pub_end and not pub_start:
            queryset = queryset.filter(
                published_year__lte=pub_end)
        elif pub_start and pub_end:
            queryset = queryset.filter(
                published_year__gte=pub_start,
                published_year__lte=pub_end)
        return queryset
