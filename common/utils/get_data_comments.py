from users.models import User, Comment
from manga.models import Manga

import random
import requests


url = "https://api.реманга.орг/api/activity/comments/?title_id=2060&page=1&ordering=-id"
domen2 = "https://api.реманга.орг/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
}


class Comments:
    help = "Parsing data from manga sites, create users and comments"

    def get_comments_data(self, *args, **kwargs):
        response = requests.get(url=url, headers=HEADERS)
        data = response.json()
        try:
            for h in Manga.objects.all():
                for i in data["content"]:
                    Comment.objects.create(
                        user=random.choice(User.objects.all()),
                        text=i["text"],
                        likes=i["count_replies"],
                        manga=h,
                    )
                return print("Comments create successfully")
        except:
            return print("Comments created")
