# MyLibrary777
ADAM PAŁUCKI, 01.2022
Example of using Google Books API.

Managing library links:
## /book/
Paginated list of books with search form
## /book/new
Validated add new book form
## /book/import
Bulk import of books from google API, using parameters mentioned in:
https://developers.google.com/books/docs/v1/using
that are:
* q - Search for volumes that contain this text string. There are special keywords you can specify in the search terms to search in particular fields, such as:
* intitle: Returns results where the text following this keyword is found in the title.
* inauthor: Returns results where the text following this keyword is found in the author.
* inpublisher: Returns results where the text following this keyword is found in the publisher.
* subject: Returns results where the text following this keyword is listed in the category list of the volume.
* isbn: Returns results where the text following this keyword is the ISBN number.
* lccn: Returns results where the text following this keyword is the Library of Congress Control Number.
* oclc: Returns results where the text following this keyword is the Online Computer Library Center number.

# API endpoints:
## restapi/all_books/
List of all books. Can add new book. Generic view. JSON data
## restapi/filtered_books/
List of all book that can be filtered by GET parameters:

* title - title of the book
* author - author name of the book
* lang - language of the publication
* pub_start - start year of publishing
* pub_end =- end year of publishing

### Development notes
To run test in development environment use command:
"python manage.py test && flake8"
