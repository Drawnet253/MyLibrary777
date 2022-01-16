# Generated by Django 4.0.1 on 2022-01-16 03:50

import core.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_book_isbn_13'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_link',
            field=models.TextField(default='https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Book_%2889362%29_-_The_Noun_Project.svg/1024px-Book_%2889362%29_-_The_Noun_Project.svg.png', validators=[core.validators.validate_cover_link]),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages_count',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]