from common.controllers import manga_controller, comments_controller, users_controller
from django.urls import path, include


urlpatterns = [
    path("getusers/", users_controller.GetDataUsers.as_view()),
    path("getmanga/", manga_controller.MangaDataParser.as_view()),
    path("getcomments/", comments_controller.CommentsDataParser.as_view()),
]
