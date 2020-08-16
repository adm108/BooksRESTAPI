from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from books.validators import validate_year


class Writer(models.Model):

    name = models.CharField(max_length=120, primary_key=True)

    def __str__(self):
        return self.name


class Genre(models.Model):

    name = models.CharField(max_length=120, primary_key=True)

    def __str__(self):
        return self.name


class Book(models.Model):

    id_field = models.SlugField(max_length=50, primary_key=True)
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Writer)
    categories = models.ManyToManyField(Genre)
    published_date = models.CharField(max_length=4, blank=True, validators=[validate_year])
    average_rating = models.DecimalField(null=True, max_digits=3, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(10.0)])
    ratings_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField(blank=True)
