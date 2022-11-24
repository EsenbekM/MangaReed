from common.utils.get_data_manga import Manga
from rest_framework import response, status
from rest_framework.views import APIView


class MangaDataParser(APIView):
    def get(self, request):
            Manga.get_data_manga(self)
            return response.Response(data="Manga data parsed", status=status.HTTP_200_OK)