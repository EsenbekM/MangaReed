from django.core.management.base import BaseCommand
import random
from users.models import User, Comment
from manga.models import Manga
import requests

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
}


url = "https://api.реманга.орг/api/activity/comments/?title_id=2060&page=1&ordering=-id"
domen = "https://api.реманга.орг/"


class Command(BaseCommand):
    help = "Create comments"

    def handle(self, *args, **kwargs):
        response = requests.get(url=url, headers=HEADERS)
        data = response.json()
        for h in Manga.objects.all():
            for i in data["content"]:
                    Comment.objects.create(
                        user=random.choice(User.objects.all()),
                        text=i["text"],
                        likes=i["count_replies"],
                        manga=h
                    )