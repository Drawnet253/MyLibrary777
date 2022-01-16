from django.urls import path
from restapi import views

app_name = 'restapi'

urlpatterns = [
    path('restapi/all_books/', views.BookList.as_view(), name='book-list'),
    path('restapi/filtered_books/', views.FilteredBookList.as_view(), name='filter-list'),
]
