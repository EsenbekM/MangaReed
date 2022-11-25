from common.utils.get_data_manga import Manga
from rest_framework import response, status
from rest_framework.views import APIView


class MangaDataParser(APIView):
    def get(self, request):
        response_data = Manga.help
        manga_controller = Manga()
        manga_controller.get_data_manga()
        return response.Response(data=response_data, status=status.HTTP_200_OK)
