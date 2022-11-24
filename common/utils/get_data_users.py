from users.models import User

import random
import requests



url = "https://api.реманга.орг/api/activity/comments/?title_id=2060&page=1&ordering=-id"
domen2 = "https://api.реманга.орг/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
}


class UserDataParser:
    help = "Parsing data from manga sites, create users and comments"

    def get_data_users(self, *args, **kwargs) -> str:
        try:
            response = requests.get(url=url, headers=HEADERS)
            data = response.json()
            for i in data["content"]:
                User.objects.create_user(
                    username=i["user"]["username"],
                    password="useruser123",
                    nickname=i["user"]["username"],
                    image=domen2 + i["user"]["avatar"]["high"],
                )
                return print("Users create successfully")
        except:
            return print("Users have been created")
      