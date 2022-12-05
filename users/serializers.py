from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=10, max_length=50)
    nickname = serializers.CharField(min_length=10, max_length=60)
    image_file = serializers.ImageField()
    password = serializers.CharField(min_length=8, max_length=40)

    class Meta:
        model = User
        fields = [
            "username",
            "nickname",
            "image_file",
            "password",
        ]
    
    
    def create(self, validated_data):
        return User.objects.create_human(
            username=validated_data["username"],
            nickname=validated_data["nickname"],
            image_file=validated_data["image_file"],
            password=validated_data["password"],
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "nickname",
            "image",
            "image_file",
        ]


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail("Invalid token")
