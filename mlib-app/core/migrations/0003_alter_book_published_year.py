# Generated by Django 4.0.1 on 2022-01-15 13:03

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_book_publication_date_book_published_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_year',
            field=models.IntegerField(default=0, validators=[core.validators.validate_published_year]),
        ),
    ]
