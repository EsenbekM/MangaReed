from django.urls import path, include
from .views import (
    MangaApiView,
    MangaDetailApiView,
    TopMangaView,
    MangaCommentsApiView,
    GenreApiView,
    AddCommentView,
)


urlpatterns = [
    path("manga/", MangaApiView.as_view(), name="manga_list_api"),
    path("manga/<pk>/", MangaDetailApiView.as_view(), name="manga_detail_api"),
    path("top-manga/", TopMangaView.as_view()),
    path("manga/<pk>/comments/", MangaCommentsApiView.as_view()),
    path("manga/<pk>/add-comment/", AddCommentView.as_view()),
    path("genre/", GenreApiView.as_view()),
]
