import django_filters
from .models import Manga


class CharFilterInFilter(
    django_filters.filters.BaseInFilter, django_filters.filters.CharFilter
):
    pass


class MangaFilter(django_filters.FilterSet):
    type = CharFilterInFilter(field_name="type", lookup_expr="in")

    class Meta:
        model = Manga
        fields = ["en_name", "ru_name", "genre__title", "type"]
