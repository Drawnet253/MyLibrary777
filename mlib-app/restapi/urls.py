from django.urls import path
from restapi import views

urlpatterns = [
    path('restapi/all_books/', views.BookList.as_view()),
    path('restapi/filtered_books/', views.FilteredBookList.as_view()),
]
