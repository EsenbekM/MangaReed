from django.core.management.base import BaseCommand
from manga.models import Genre

import requests


# genre_url = "https://api.реманга.орг/api/forms/titles/?get=genres&get=categories&get=types&get=status&get=age_limit"
# HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
# }


# class Command(BaseCommand):
#     help = "Parsing data from manga sites, create users and comments"

#     def handle(self, *args, **kwargs):
#         genre_response = requests.get(url=genre_url, headers=HEADERS)
#         genre_data = genre_response.json()
#         for i in genre_data["content"]["genres"]:
#             try:
#                 Genre.objects.create(title=i["name"])
#             except:
#                 return "Genre - {}".format(False)
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
}
domen = "https://remanga.org/media/"


class Command(BaseCommand):
    help = "Parsing manga"

    def handle(self, *args: any, **options: any) -> object:
        Genre.objects.create(
            self_id= "0",
            title="Боевик"                                                      
        )
        Genre.objects.create(
            self_id= "1",
            title="Боевые искусства"
        )
        Genre.objects.create(
            self_id="2",
            title="Гарем"
        )
        Genre.objects.create(
            title="Гендерная интрига"
        )
        Genre.objects.create(
            title="Героическое фэнтези"
        )
        Genre.objects.create(
            title="Детектив"
        )
        Genre.objects.create(
            title="Дзёсэй"
        )
        Genre.objects.create(
            title="Детектив"
        )
        Genre.objects.create(
            title="Додзинси"
        )
        Genre.objects.create(
            title="Игра"
        )
        Genre.objects.create(
            title="История"
        )
        Genre.objects.create(
            title="Киберпанк"
        )
        Genre.objects.create(
            title="Кодомо"
        )
        Genre.objects.create(
            title="Комедия"
        )
        Genre.objects.create(
            title="Меха"
        )
        Genre.objects.create(
            title="Мистика"
        )
        Genre.objects.create(
            title="Мурим"
        )
        Genre.objects.create(
            title="Научная фантастика"
        )
        Genre.objects.create(
            title="Повседневность"
        )
        Genre.objects.create(
            title="Постапокалиптика"
        )
        Genre.objects.create(
            title="Приключения"
        )
        Genre.objects.create(
            title="Психология"
        )
        Genre.objects.create(
            title="Романтика"
        )
        Genre.objects.create(
            title="Сверхъестественное"
        )
        Genre.objects.create(
            title="Сёдзё"
        )
        Genre.objects.create(
            title="Сёдзё-ай"
        )
        Genre.objects.create(
            title="Сёнэн"
        )
        Genre.objects.create(
            title="Спорт"
        )
        Genre.objects.create(
            title="Фантастика"
        )
        Genre.objects.create(
            title="Фэнтези"
        )
        Genre.objects.create(
            title="Школа"
        )
        Genre.objects.create(
            title="Элементы юмора"
        )
        Genre.objects.create(
            title="Этти"
        )
        Genre.objects.create(
            title="Яой"
        )


        
