# BooksRESTAPI

## Description:
It's a simple books REST API that allows to:
- display list of all books
- sort and filtr books by year
- dispaly list of books selected authors
- display selected book

This app has an additional ability to download data set from: https://www.googleapis.com/books/v1/volumes?q=war (thanks to request library) and create or update instances in the database.

## Technologies and libraries:
- Python 3.8.5
- Django 3.1
- Django Rest Framework 3.11.1
- django-filter 2.3.0
- request 2.24.0
- HTML 5 and CSS 3 (basic view with a button that adds data from Google API to the database and urls endpoints)

## Installation:
##### 1. Clone repository:
```sh
$ git clone https://github.com/adm108/BooksRESTAPI.git
```
##### 2. Create virtual enviroment and activate it:
```sh
$ python -m venv venv (if you work on Windows system)
```
##### 3. Go to BooksRESTAPI:
```sh
$ cd BooksRESTAPI
```
##### 4. Install all packages from requirements.txt file:
```sh
$ pip install -r requirements.txt
```
##### 5. Go to BooksRESTAPI folder and use manage.py to enter following commands. Generate SQL commands:
```sh
$ python manage.py makemigrations
```
##### 6. Execute SQL commands:
```sh
$ python manage.py migrate
```
##### 7. Create superuser (enter email, username and password):
```sh
$ python manage.py createsuperuser
```
##### 8. Add data via shell from Google API (https://www.googleapis.com/books/v1/volumes?q=Hobbit), go to shell via terminal, copy prepared data (available below) and paste it:
```sh
$ python manage.py shell
```
```sh
from books.models import Writer, Genre, Book

a1 = Writer(name="John Ronald Reuel Tolkien")
a2 = Writer(name="J. R. R. Tolkien")
a3 = Writer(name="Devin Brown")
a4 = Writer(name="Corey Olsen")
a5 = Writer(name="Perry C. Bramlett")
a6 = Writer(name="Jim Ware")
a7 = Writer(name="William Howard Green")
a8 = Writer(name="Jude Fisher")
a9 = Writer(name="Ed Strauss")

a1.save()
a2.save()
a3.save()
a4.save()
a5.save()
a6.save()
a7.save()
a8.save()
a9.save()

c1 = Genre(name="Baggins, Bilbo (Fictitious character)")
c2 = Genre(name="Literary Criticism")
c3 = Genre(name="FICTION")
c4 = Genre(name="Biography & Autobiography")
c5 = Genre(name="Religion")
c6 = Genre(name="Art")

c1.save()
c2.save()
c3.save()
c4.save()
c5.save()
c6.save()

b1 = Book(id_field="DqLPAAAAMAAJ", title="Hobbit czyli Tam i z powrotem", published_date="1985", average_rating=None, ratings_count=0, thumbnail="http://books.google.com/books/contentid=DqLPAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api")
b1.save()
b1.authors.add(a1)

b2 = Book(id_field="YyXoAAAACAAJ", title="Hobbit czyli Tam i z powrotem", published_date="2004", average_rating=5.0, ratings_count=2, thumbnail="http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api")
b2.save()
b2.authors.add(a2)
b2.categories.add(c1)

b3 = Book(id_field="QMZ-SpsAuasC", title="The Christian World of The Hobbit", published_date="2012", average_rating=4.5, ratings_count=5, thumbnail="http://books.google.com/books/content?id=QMZ-SpsAuasC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api")
b3.save()
b3.authors.add(a3)
b3.categories.add(c2)

b4 = Book(id_field="KY0BDObXftUC", title="Exploring J.R.R. Tolkien's The Hobbit", published_date="2012", average_rating=4.0, ratings_count=8, thumbnail="http://books.google.com/books/content?id=KY0BDObXftUC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api")
b4.save()
b4.authors.add(a4)
b4.categories.add(c2)

b5 = Book(id_field="hFfhrCWiLSMC", title="The Hobbit, Or, There and Back Again", published_date="1982", average_rating=4.0, ratings_count=2649, thumbnail="http://books.google.com/books/content?id=hFfhrCWiLSMC&printsec=frontcover&img=1&zoom=1&source=gbs_api")
b5.save()
b5.authors.add(a1)
b5.categories.add(c3)

b6 = Book(id_field="8ef3-s6fixIC", title="I Am in Fact a Hobbit", published_date="2003", average_rating=5.0, ratings_count=2, thumbnail="http://books.google.com/books/content?id=8ef3-s6fixIC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api")
b6.save()
b6.authors.add(a5)
b6.categories.add(c4)

b7 = Book(id_field="N_0VhzQKIIAC", title="Finding God in the Hobbit", published_date="2006", average_rating=4.5, ratings_count=13, thumbnail="http://books.google.com/books/content?id=N_0VhzQKIIAC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api")
b7.save()
b7.authors.add(a6)
b7.categories.add(c5)

b8 = Book(id_field="CSUeAQAAIAAJ", title="The Hobbit", published_date="1995", average_rating=None, ratings_count=0, thumbnail="http://books.google.com/books/content?id=CSUeAQAAIAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api")
b8.save()
b8.authors.add(a7)
b8.categories.add(c2)

b9 = Book(id_field="H8ON-dTgQQYC", title="The Hobbit", published_date="2012", average_rating=4.5, ratings_count=8, thumbnail="http://books.google.com/books/content?id=H8ON-dTgQQYC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api")
b9.save()
b9.authors.add(a8)
b9.categories.add(c6)

b10 = Book(id_field="KUSn4G6eiCUC", title="A Hobbit Devotional", published_date="2012", average_rating=4.0, ratings_count=7, thumbnail="http://books.google.com/books/content?id=KUSn4G6eiCUC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api")
b10.save()
b10.authors.add(a9)
b10.categories.add(c5)
```
##### 9. Run your local server:
```sh
$ python manage.py runserver
```
##### 10. Now you can add data via upload button which is available on the main side (thanks to request library which collects data from that Google API: https://www.googleapis.com/books/v1/volumes?q=war). On the main site are available other urls endpoints.

##### 11. Now you can test my app! It is available on pythonanywhere site:
http://adm108.pythonanywhere.com/
