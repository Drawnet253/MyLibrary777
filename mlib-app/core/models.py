from django.db import models
from .validators import validate_title, validate_isbn13, validate_pub_lang
from .validators import validate_pages_count, validate_cover_link
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    """Book model"""
    title = models.CharField(max_length=255, validators=[validate_title])
    authors = models.ManyToManyField('Author')
    isbn_13 = models.IntegerField(validators=[validate_isbn13])
    cover_link = models.TextField(validators=[validate_cover_link])
    pages_count = models.IntegerField(validators=[validate_pages_count])
    publication_language = models.CharField(
            max_length=2,
            validators=[validate_pub_lang]
    )
    published_year = models.IntegerField(
            default=0,
            validators=[MinValueValidator(0), MaxValueValidator(2022)]
    )

    def __str__(self):
        return self.title


class Author(models.Model):
    """Author model to connect with books"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
