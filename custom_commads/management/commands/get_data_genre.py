from django.core.management.base import BaseCommand
from manga.models import Genre
from bs4 import BeautifulSoup

import requests

class Command(BaseCommand):
    help = "Create genres"
    def handle(self, *args, **kwargs):
        Genre.objects.get_or_create(title="Боевик")
        Genre.objects.get_or_create(title="Гарем")
        Genre.objects.get_or_create(title="Детектив")
        Genre.objects.get_or_create(title="Гарем")
        Genre.objects.get_or_create(title="Гендерная интрига")
        Genre.objects.get_or_create(title="Героическое фэнтези")
        Genre.objects.get_or_create(title="Детектив")
        Genre.objects.get_or_create(title="Дзёсэй")
        Genre.objects.get_or_create(title="Додзинси")
        Genre.objects.get_or_create(title="Драма")
        Genre.objects.get_or_create(title="Игра")
        Genre.objects.get_or_create(title="История")
        Genre.objects.get_or_create(title="Киберпанк")
        Genre.objects.get_or_create(title="Кодомо")
        Genre.objects.get_or_create(title="Комедия")
        Genre.objects.get_or_create(title="Махо-сёдзё")
        Genre.objects.get_or_create(title="Меха")
        Genre.objects.get_or_create(title="Мистика")
        Genre.objects.get_or_create(title="Мурим")
        Genre.objects.get_or_create(title="Научная фантастика")
        Genre.objects.get_or_create(title="Повседневность")
        Genre.objects.get_or_create(title="Постапокалиптика")
        Genre.objects.get_or_create(title="Приключения")
        Genre.objects.get_or_create(title="Психология")
        Genre.objects.get_or_create(title="Романтика")
        Genre.objects.get_or_create(title="Сверхъестественное")
        Genre.objects.get_or_create(title="Сёдзё")
        Genre.objects.get_or_create(title="Сёдзё-ай")
        Genre.objects.get_or_create(title="Сёнэн")
        Genre.objects.get_or_create(title="Сёнэн-ай")
        Genre.objects.get_or_create(title="Спорт")
        Genre.objects.get_or_create(title="Сэйнэн")
        Genre.objects.get_or_create(title="Трагедия")
        Genre.objects.get_or_create(title="Триллер")
        Genre.objects.get_or_create(title="Ужасы")
        Genre.objects.get_or_create(title="Фантастика")
        Genre.objects.get_or_create(title="Фэнтези")
        Genre.objects.get_or_create(title="Школа")
        Genre.objects.get_or_create(title="Элементы юмора")
        Genre.objects.get_or_create(title="Этти")
        Genre.objects.get_or_create(title="Юри")
        Genre.objects.get_or_create(title="Яой")


        
        