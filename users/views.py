from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework import status, views, generics, response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .serializers import (
    UserRegisterSerializer,
    LoginSerializer,
    ProfileSerializer,
    LogoutSerializer,
)
from .models import User
from common.shemas import users


class RegisterApiView(views.APIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = []
    authentication_classes = []
    schema = users.SignUpSchema()

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            response_data = {
                "status": status.HTTP_201_CREATED,
                "username": request.data["username"],
                "nickname": request.data["nickname"],
                "message": "Register successfully",
            }
            serializer.save()
            return response.Response(data=response_data)


class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    schema = users.SignInSchema()
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                username = request.data["username"]
                password = request.data["password"]
                user = authenticate(username=username, password=password)
                if user is None:
                    return response.Response("User not found, try again body!")

                access = AccessToken.for_user(user)
                refresh = RefreshToken.for_user(user)
                response_data = {
                    "status": status.HTTP_200_OK,
                    "user": username,
                    "access": str(access),
                    "refresh": str(refresh),
                }
                return response.Response(data=response_data)

            return response.Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        except:
            return response.Response(
                data={
                    "message": "Упс, что-то пошло не так! Попробуй в другой раз Т_Т",
                    "error": "Not found error",
                }
            )


# class UserProfileView(views.APIView):
#     queryset = User.objects.all()
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = ProfileSerializer

#     def get(self, request, pk):
#         user = get_object_or_404(User, pk=pk)
#         serializer = self.serializer_class(
#             user, many=False, context={"request": request}
#         ).data
#         return response.Response(data=serializer, status=status.HTTP_200_OK)


# class UsersListApiView(generics.ListAPIView):
#     queryset = User.objects.all()
#     permission_classes = []
#     serializer_class = ProfileSerializer
#     authentication_classes = []


class LogoutApiView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(data="Logouted", status=status.HTTP_204_NO_CONTENT)


# Create your views here.
