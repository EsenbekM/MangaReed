from common.utils.get_data_users import UserDataParser
from rest_framework.views import APIView
from users.models import User
from rest_framework import response, status


class GetDataUsers(APIView):
    def get(self, request):
        response_data = UserDataParser.help
        users_controller = UserDataParser()
        users_controller.get_data_users(self)
        return response.Response(data=response_data, status=status.HTTP_200_OK)
