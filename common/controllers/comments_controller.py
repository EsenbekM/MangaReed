from common.utils.get_data_comments import Comment
from rest_framework import response, status
from rest_framework.views import APIView


class CommentsDataParser(APIView):
    def get(self, request):
        try:
            response_data = "Get users data successfully"
            Comment.get_comments_data(self)
            return response.Response(data=response_data, status=status.HTTP_200_OK)
        except:
            return response.Response(data="Unregistered error", status=status.HTTP_400_BAD_REQUEST)