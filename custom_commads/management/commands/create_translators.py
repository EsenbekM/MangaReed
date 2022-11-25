from django.core.management.base import BaseCommand
import random
from manga.models import Manga, Genre, Translator
from users.models import User, Comment
import requests


class Command(BaseCommand):
    help = "Parsing data from manga sites, create users and comments"

    def handle(self, *args, **kwargs):
        Translator.objects.create(
            title="Tiny Team",
        )
        Translator.objects.create(
            title="AniDub",
        )
        Translator.objects.create(
            title="AniRead",
        )
        Translator.objects.create(
            title="Kubik",
        )
        Translator.objects.create(
            title="Snow Birds",
        )
        Translator.objects.create(
            title="Moon Time",
        )
        Translator.objects.create(
            title="Animaxa",
        )
        
        
