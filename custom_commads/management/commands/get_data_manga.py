from django.core.management.base import BaseCommand
import random
from manga.models import Manga, Genre, Translator
from users.models import User, Comment
import requests
import json


# genre_url = "https://api.реманга.орг/api/forms/titles/?get=genres&get=categories&get=types&get=status&get=age_limit"
# uri = "https://api.newmanga.org/v2/projects/popular?scale=week&page=1&size=250"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
}
domen = "https://remanga.org/media/"


class Command(BaseCommand):
    help = "Parsing manga"

    def handle(self, *args: any, **options: any) -> object:
        for i in range(1, 100):
            url = (
                "https://api.remanga.org/api/titles/recommendations/?&count=20&page="
                + str(i)
            )
            request = requests.get(url=url, headers=HEADERS)
            request_data = request.json()
            content_data = request_data["content"]

            for item in request_data["content"]:
                content_data = (g for g in request_data["content"])
                content_data = list(content_data)
                genre_filter_set = item["genres"]
                for i in genre_filter_set:
                    global genre_filter_id
                    genre_filter_name = i["name"]

                manga = Manga.objects.create(
                    en_name=item["en_name"],
                    ru_name=item["rus_name"],
                    image=domen + item["cover_high"],
                    type=item["type"],
                    issue_year=item["issue_year"],
                    rating=item["avg_rating"],
                    likes=item["total_votes"],
                    chapters_quantity=item["count_chapters"],
                )
                manga.genre.set(Genre.objects.filter(title=genre_filter_name))
                

# domen = "https://img.newmanga.org/ProjectCard/webp/"
#
#
# class Command(BaseCommand):
# help = "Parsing data from manga sites, create users and comments"
#
# def handle(self, *args, **kwargs):
# manga_response = requests.get(url=uri, headers=HEADERS)
# manga_data = manga_response.json()
# for i in manga_data["items"]:
# Manga.objects.create(
# en_name=i["title"]["en"],
# ru_name=i["title"]["ru"],
# description=i["description"],
# image=domen + i["image"]["name"],
# type=i["type"],
# likes=i["hearts"],
# rating=i["rating"],
# ).genre.set(random.choices(Genre.objects.all()))
