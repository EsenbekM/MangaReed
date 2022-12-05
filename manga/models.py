from django.db import models
from .settings import rating_choices, genre_choices


class Genre(models.Model):
    self_id = models.PositiveIntegerField(null=True)
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.title


class Manga(models.Model):
    en_name = models.CharField(max_length=200, unique=True)
    ru_name = models.CharField(max_length=200, unique=True)
    image = models.TextField()
    description = models.TextField()
    genre = models.ManyToManyField(Genre)
    chapters_quantity = models.PositiveIntegerField(null=True)
    issue_year = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=100)
    likes = models.PositiveIntegerField()
    rating = models.FloatField(default=0.0, blank=True)

    class Meta:
        verbose_name = "Манга"
        verbose_name_plural = "Манга"

    def __str__(self):
        return self.en_name


# Create your models here.
