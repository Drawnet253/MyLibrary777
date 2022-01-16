from . import views
from django.urls import path


urlpatterns = [
    # /book/
    path('', views.BooksListView.as_view(), name='index'),
    # /book/new
    path('new/', views.CreateBookView.as_view(), name='book_new'),
    # /book/import
    path('import/', views.BooksImportView.as_view(), name='import'),
    # /book/books_import
    path('books_import/', views.books_import, name='books_import'),
]
