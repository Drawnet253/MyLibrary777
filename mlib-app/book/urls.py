from . import views
from django.urls import path


urlpatterns = [
    # /book/
    path('', views.BooksListView.as_view(), name='index'),
]
