from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from django.shortcuts import render, redirect
from django.contrib import messages

from books.api.serializers import BookSerializer
from books.models import Book, Writer, Genre

import requests


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    lookup_field = "id_field"
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['published_date', 'authors']
    ordering_fields = ['published_date']



def post_db(request):
    template = 'index.html'

    if request.method == 'GET':
        return render(request, template)

    response = requests.get("https://www.googleapis.com/books/v1/volumes?q=war")
    if response.status_code != 200:
        messages.error(request, 'There is some problem with the API site, status code: ' + str(response.status_code))
        return redirect('upload')

    data = response.json()
    authors = []
    categories = []

    for element in data['items']:
        try:
            for member in element['volumeInfo']['authors']:
                if Writer.objects.filter(name=member).exists():
                    authors.append(member)
                else:
                    authors.append(member)
                    Writer.objects.create(name=member)
        except KeyError:
            pass
        try:
            for item in element['volumeInfo']['categories']:
                if Genre.objects.filter(name=item).exists():
                    categories.append(item)
                else:
                    categories.append(item)
                    Genre.objects.create(name=item)
        except KeyError:
            pass
        
        if Book.objects.filter(id_field=element['id']).exists():
            instance = Book.objects.get(id_field=element['id'])
            instance.authors.clear()
            instance.categories.clear()

            try:
                average_rating=element['volumeInfo']['averageRating']
            except KeyError:
                average_rating=None
            try:
                ratings_count=element['volumeInfo']['ratingsCount']
            except KeyError:
                ratings_count=0
            try:
                thumbnail=element['volumeInfo']['imageLinks']['thumbnail']
            except KeyError:
                thumbnail=""

            Book.objects.filter(id_field=element['id']).update(
                id_field=element['id'],
                title=element['volumeInfo']['title'],
                published_date=element['volumeInfo']['publishedDate'][0:4],
                average_rating=average_rating,
                ratings_count=ratings_count,
                thumbnail=thumbnail
                )
            
            instance = Book.objects.get(id_field=element['id'])
            for element in authors:
                instance.authors.add(Writer.objects.get(name=element))
            for element in categories:
                instance.categories.add(Genre.objects.get(name=element))
            authors = []
            categories = []

        else:
            try:
                average_rating=element['volumeInfo']['averageRating']
            except KeyError:
                average_rating=None
            try:
                ratings_count=element['volumeInfo']['ratingsCount']
            except KeyError:
                ratings_count=0

            Book.objects.create(
                id_field=element['id'],
                title=element['volumeInfo']['title'],
                published_date=element['volumeInfo']['publishedDate'][0:4],
                average_rating=average_rating,
                ratings_count=ratings_count,
                thumbnail=element['volumeInfo']['imageLinks']['thumbnail']
                )
            instance = Book.objects.get(id_field=element['id'])
            for element in authors:
                instance.authors.add(Writer.objects.get(name=element))
            for element in categories:
                instance.categories.add(Genre.objects.get(name=element))
            authors = []
            categories = []
            
    messages.success(request, 'Books from the database have been updated!')
    return redirect('upload')
