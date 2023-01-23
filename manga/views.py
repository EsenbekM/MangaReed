from django.shortcuts import get_object_or_404
from rest_framework import views, status, generics, response, permissions
from .models import Manga, Genre
from users.models import Comment
from .serializers import (
    MangaSerializer,
    MangaDetailSerializer,
    GenreSerializer,
    CommentSerializer,
    CommentAddSerializer,
    LikeCommentSerializer,
)

from rest_framework.filters import SearchFilter
from .paginations import MangaPagination, TopMangaPagination
import django_filters
from common.shemas import manga


class MangaApiView(generics.ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        SearchFilter,
    ]
    search_fields = ["en_name", "ru_name", "type", "genre__title"]
    filterset_fields = ["type", "genre__title", "en_name", "ru_name"]
    schema = manga.MangaListShema()
    # pagination_class = MangaPagination


class MangaDetailApiView(generics.GenericAPIView):
    serializer_class = MangaDetailSerializer
    schema = manga.MangaDetailShema()

    def get(self, request, pk):
        instance = get_object_or_404(Manga, pk=pk)
        serializer = self.serializer_class(
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
    schema = manga.MangaListShema()


class MangaCommentsApiView(generics.GenericAPIView):
    serializer_class = CommentSerializer
    schema = manga.MangaCommentsList()

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


class AddCommentView(generics.GenericAPIView):
    serializer_class = CommentAddSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    schema = manga.MangaAddCommentSchema()

    def post(self, request, pk):
        if request.user.is_authenticated:
            manga = get_object_or_404(Manga, pk=pk)
            serializer = self.get_serializer(data=request.data)
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
