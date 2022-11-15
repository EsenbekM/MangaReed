import requests
from bs4 import BeautifulSoup
import time
import json

# from manga.models import Manga, Genre
from random import choices


url = "https://mintmanga.live/list/translators/sort_rate"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
}


def get_html(url):
    request = requests.get(url=url, headers=HEADERS)
    return request


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="leftContent")
    data = []
    for i in items:
        data.append({
        "translator": i.find("table", class_="table table-hover").find("a", class_="person-link").get_text()
        })
    print(data)


html = get_html(url)
get_data(html.text)