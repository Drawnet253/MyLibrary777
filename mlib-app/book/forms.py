from django import forms
from core.models import Book, Author
from core.validators import validate_title, validate_isbn13
from core.validators import validate_pub_lang
from core.validators import validate_cover_link
from django.core.validators import MaxValueValidator, MinValueValidator


class CreateBookForm(forms.ModelForm):
    '''POST Form to create the book '''

    class Meta:
        model = Book
        fields = ['title', 'authors', 'pages_count', 'isbn_13',
                  'publication_language', 'cover_link', 'published_year']

    title = forms.CharField(
        label='(*)Title of the book',
        max_length=255,
        help_text='Required field. Please enter 2-255 characters.',
        validators=[validate_title])
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        initial='0',
        widget=forms.SelectMultiple(),
        required=True,
        label='(*)Choose authors',
        help_text='''
            possible multiple choice with holding CTRL (Windows)
                 or Command (MacOS)''')
    isbn_13 = forms.IntegerField(
            label='(*)ISBN-13',
            validators=[validate_isbn13,
                        MinValueValidator(0),
                        MaxValueValidator(9999999999999)
                        ],
            help_text='Required field. Please enter 13 digits.'
    )
    cover_link = forms.CharField(
            label='Link to the cover image',
            widget=forms.Textarea(
                attrs={'rows': '4'}
                ),
            required=False,
            validators=[validate_cover_link],
            help_text='Please paste link to the cover image'
    )
    pages_count = forms.IntegerField(
            label='(*)Number of pages',
            validators=[MinValueValidator(0)]
    )
    publication_language = forms.CharField(
        label='(*)Publication Language',
        max_length=2,
        help_text='Only two letters - country code',
        validators=[validate_pub_lang]
    )
    published_year = forms.IntegerField(
            label='Publication Year',
            validators=[MinValueValidator(0), MaxValueValidator(2022)]
    )


class SearchForm(forms.ModelForm):
    '''Search form - GET'''

    class Meta:
        model = Book
        fields = ['title', 'authors', 'pages_count', 'isbn_13',
                  'publication_language', 'cover_link', 'published_year']

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['book_title'] = self.get_queryset()
        context['book_author'] = self.get_queryset()
        context['language'] = self.get_queryset()
        context['from_date'] = self.get_queryset()
        context['to_date'] = self.get_queryset()
        return context


class ImportBooksForm(forms.ModelForm):
    '''POST Form to ask for keywords for Google API'''

    class Meta:
        model = Book
        fields = ['title', 'authors', 'pages_count', 'isbn_13',
                  'publication_language', 'cover_link', 'published_year']

    def get_context_data(self, **kwargs):
        context = super(BooksImportView, self).get_context_data(**kwargs)
        context['keywords'] = self.get_queryset()
        context['intitle'] = self.get_queryset()
        context['inauthor'] = self.get_queryset()
        context['inpublisher'] = self.get_queryset()
        context['subject'] = self.get_queryset()
        context['isbn'] = self.get_queryset()
        context['lccn'] = self.get_queryset()
        context['oclc'] = self.get_queryset()
        return context
