import requests
from bs4 import BeautifulSoup
import time
import json
from manga.models import Manga, Genre
from random import choices


url = "https://api.реманга.орг/api/search/catalog/?ordering=-rating&count=250"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
}


def get_genres():
    response = requests.get(
        url="https://api.реманга.орг/api/forms/titles/?get=genres&get=categories&get=types&get=status&get=age_limit",
        headers=HEADERS,
    )
    data = response.json()
    for i in data["content"]:
        Genre.objects.create(title=i["name"])


def get_api():
    response = requests.get(url=url, headers=HEADERS)
    data = response.json()
    for i in data["content"]:
        Manga.objects.create(
            en_name=i["en_name"],
            ru_name=i["rus_name"],
            image=i["img"]["mid"],
            genre=choices(Genre.objects.all()),
        )


if __name__ == "__main__":
    get_genres()
    get_api()
