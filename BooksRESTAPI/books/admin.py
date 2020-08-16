from django.contrib import admin
from books.models import Writer, Genre, Book

admin.site.register(Writer)
admin.site.register(Genre)
admin.site.register(Book)