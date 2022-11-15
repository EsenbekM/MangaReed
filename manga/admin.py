from django.contrib import admin
from .models import Manga, Genre, Translator


admin.site.register(Manga)
admin.site.register(Genre)
admin.site.register(Translator)
# Register your models here.
