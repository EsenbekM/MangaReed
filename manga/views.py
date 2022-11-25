from django.shortcuts import render, get_object_or_404
from rest_framework import views, status, generics, response
from .models import Manga, Genre, Translator
from .serializers import (
    MangaSerializer,
    MangaDetailSerializer,
    GenreSerializer,
    CommentSerializer,
    CommentAddSerializer,
)
from .filters import MangaFilter
from rest_framework.filters import SearchFilter
from .paginations import MangaPagination, TopMangaPagination, GenrePagination
import django_filters
from common.schemas.manga import GetMangaSchema


class MangaApiView(generics.ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        SearchFilter,
    ]
    search_fields = ["en_name", "ru_name", "type", "genre__title"]
    filterset_fields = ["type", "genre__title", "en_name", "ru_name"]
    schema = GetMangaSchema()
    pagination_class = MangaPagination


class MangaDetailApiView(views.APIView):
    def get(self, request, pk):
        instance = get_object_or_404(Manga, pk=pk)
        serializer = MangaDetailSerializer(
            instance, many=False, context={"request": request}
        ).data
        return response.Response(data=serializer, status=status.HTTP_200_OK)


class TopMangaView(generics.ListAPIView):
    queryset = Manga.objects.order_by("-rating")
    serializer_class = MangaSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        SearchFilter,
    ]
    search_fields = ["en_name", "ru_name", "type", "genre__title"]
    filterset_fields = ["type", "genre__title", "en_name", "ru_name"]
    pagination_class = TopMangaPagination


class MangaCommentsApiView(views.APIView):
    serializer_class = CommentSerializer

    def get(self, request, pk):
        manga = get_object_or_404(Manga, pk=pk)
        comments_data = self.serializer_class(
            manga.manga_comments, many=True, context={"request": request}
        ).data

        return response.Response(data=comments_data)


class GenreApiView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = []
    authentication_classes = []
    # pagination_class = GenrePagination


class AddCommentView(views.APIView):
    def post(self, request, pk):
        if request.user.is_authenticated:
            manga = get_object_or_404(Manga, pk=pk)
            serializer = CommentAddSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    manga=manga, user=request.user, text=request.data["text"]
                )
                return response.Response(
                    data=request.data, status=status.HTTP_201_CREATED
                )
        return response.Response(
            data={"message": "Not authorized error"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


"""

[
    {
        "id": 1,
        "title": "Боевик"
    },
    {
        "id": 2,
        "title": "Боевые искусства"
    },
    {
        "id": 3,
        "title": "Гарем"
    },
    {
        "id": 4,
        "title": "Гендерная интрига"
    },
    {
        "id": 5,
        "title": "Героическое фэнтези"
    },
    {
        "id": 6,
        "title": "Детектив"
    },
    {
        "id": 7,
        "title": "Дзёсэй"
    },
    {
        "id": 8,
        "title": "Додзинси"
    },
    {
        "id": 9,
        "title": "Драма"
    },
    {
        "id": 10,
        "title": "Игра"
    },
    {
        "id": 11,
        "title": "История"
    },
    {
        "id": 12,
        "title": "Киберпанк"
    },
    {
        "id": 13,
        "title": "Кодомо"
    },
    {
        "id": 14,
        "title": "Комедия"
    },
    {
        "id": 15,
        "title": "Махо-сёдзё"
    },
    {
        "id": 16,
        "title": "Меха"
    },
    {
        "id": 17,
        "title": "Мистика"
    },
    {
        "id": 18,
        "title": "Мурим"
    },
    {
        "id": 19,
        "title": "Научная фантастика"
    },
    {
        "id": 20,
        "title": "Повседневность"
    },
    {
        "id": 21,
        "title": "Постапокалиптика"
    },
    {
        "id": 22,
        "title": "Приключения"
    },
    {
        "id": 23,
        "title": "Психология"
    },
    {
        "id": 24,
        "title": "Романтика"
    },
    {
        "id": 25,
        "title": "Сверхъестественное"
    },
    {
        "id": 26,
        "title": "Сёдзё"
    },
    {
        "id": 27,
        "title": "Сёдзё-ай"
    },
    {
        "id": 28,
        "title": "Сёнэн"
    },
    {
        "id": 29,
        "title": "Сёнэн-ай"
    },
    {
        "id": 30,
        "title": "Спорт"
    },
    {
        "id": 31,
        "title": "Сэйнэн"
    },
    {
        "id": 32,
        "title": "Трагедия"
    },
    {
        "id": 33,
        "title": "Триллер"
    },
    {
        "id": 34,
        "title": "Ужасы"
    },
    {
        "id": 35,
        "title": "Фантастика"
    },
    {
        "id": 36,
        "title": "Фэнтези"
    },
    {
        "id": 37,
        "title": "Школа"
    },
    {
        "id": 38,
        "title": "Элементы юмора"
    },
    {
        "id": 39,
        "title": "Этти"
    },
    {
        "id": 40,
        "title": "Юри"
    },
    {
        "id": 41,
        "title": "Яой"
    }


"""
