from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status, views, generics, response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .serializers import UserRegisterSerializer, LoginSerializer
from .models import User


class RegisterApiView(views.APIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            response_data = {
                "status": status.HTTP_201_CREATED,
                "username": request.data["username"],
                "nickname": request.data["nickname"],
                "message": "Register successfully, welcome to the club body!",
            }
            serializer.save()
            return response.Response(data=response_data)


class LoginApiView(views.APIView):
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data).data
            if serializer.is_valid():
                username = request.data["username"]
                password = request.data["password"]
                user = authenticate(username=username, password=password)
                if user is None:
                    raise ValueError("User not found, try again body!")

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
                data="Упс, что-то пошло не так! Попробуй в другой раз Т_Т"
            )


# Create your views here.
