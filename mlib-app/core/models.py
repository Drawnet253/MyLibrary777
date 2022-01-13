from django.db import models


class Book(models.Model):
    """Book model"""
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('Author')
    isbn_13 = models.CharField(max_length=13)
    cover_link = models.TextField()
    pages_count = models.IntegerField()
    publication_language = models.CharField(max_length=2)

    def __str__(self):
        return self.title


class Author(models.Model):
    """Author model to connect with books"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
