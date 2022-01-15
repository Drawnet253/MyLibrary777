from . import views
from django.urls import path


urlpatterns = [
    # /book/
    path('', views.BooksListView.as_view(), name='index'),
    path('new/', views.CreateBookView.as_view(), name='book_new'),
]
