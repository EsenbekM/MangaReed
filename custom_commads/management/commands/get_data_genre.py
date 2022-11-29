from django.core.management.base import BaseCommand
from manga.models import Genre

import requests


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
}
domen = "https://remanga.org/media/"


class Command(BaseCommand):
    help = "Parsing manga"

    def handle(self, *args: any, **options: any) -> object:
        Genre.objects.get_or_create(self_id="0", title="Боевик")
        Genre.objects.get_or_create(self_id="1", title="Боевые искусства")
        Genre.objects.get_or_create(self_id="2", title="Гарем")
        Genre.objects.get_or_create(title="Гендерная интрига")
        Genre.objects.get_or_create(title="Героическое фэнтези")
        Genre.objects.get_or_create(title="Детектив")
        Genre.objects.get_or_create(title="Дзёсэй")
        Genre.objects.get_or_create(title="Детектив")
        Genre.objects.get_or_create(title="Додзинси")
        Genre.objects.get_or_create(title="Игра")
        Genre.objects.get_or_create(title="История")
        Genre.objects.get_or_create(title="Киберпанк")
        Genre.objects.get_or_create(title="Кодомо")
        Genre.objects.get_or_create(title="Комедия")
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
        Genre.objects.get_or_create(title="Спорт")
        Genre.objects.get_or_create(title="Фантастика")
        Genre.objects.get_or_create(title="Фэнтези")
        Genre.objects.get_or_create(title="Школа")
        Genre.objects.get_or_create(title="Элементы юмора")
        Genre.objects.get_or_create(title="Этти")
        Genre.objects.get_or_create(title="Яой")
