from rest_framework import serializers
from books.models import Book, Genre, Writer


class BookSerializer(serializers.ModelSerializer):

    authors = serializers.SlugRelatedField(queryset=Writer.objects.all(), many=True, slug_field='name')
    categories = serializers.SlugRelatedField(queryset=Genre.objects.all(), many=True, slug_field='name')

    class Meta:
        model = Book
        fields = ['id_field', 'title', 'authors', 'categories', 'published_date', 'average_rating', 'ratings_count', 'thumbnail']
