from django.core.management.base import BaseCommand
import random
from manga.models import Manga, Genre
import requests
import json


manga_url = "https://api.реманга.орг/api/search/catalog/?ordering=-rating&count=250"
genre_url = "https://api.реманга.орг/api/forms/titles/?get=genres&get=categories&get=types&get=status&get=age_limit"
uri = "https://api.newmanga.org/v2/projects/popular?scale=week&page=1&size=100"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
}
domen = "https://img.newmanga.org/ProjectCard/webp/"


class Command(BaseCommand):
    help = "Parsing data from managlib"

    def handle(self, *args, **kwargs):
        genre_response = requests.get(url=genre_url, headers=HEADERS)
        genre_data = genre_response.json()
        for i in genre_data["content"]["genres"]:
            Genre.objects.create(title=i["name"])

        manga_response = requests.get(url=uri, headers=HEADERS)
        manga_data = manga_response.json()
        for i in manga_data["items"]:
            Manga.objects.create(
                en_name=i["title"]["en"],
                ru_name=i["title"]["ru"],
                description=i["description"],
                image=domen + i["image"]["name"],
                type=i["type"],
                rating=i["rating"],
            ).genre.set(random.choices(Genre.objects.all()))
