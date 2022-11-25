from django.urls import path
from .views import (
    RegisterApiView,
    LoginApiView,
    UserProfileView,
    LogoutApiView,
    UsersListApiView,
)


urlpatterns = [
    path("signup/", RegisterApiView.as_view(), name="register_api"),
    path("signin/", LoginApiView.as_view(), name="login_api"),
    path("logout/", LogoutApiView.as_view(), name="logout_api"),
    path("profile/<pk>/", UserProfileView.as_view(), name="profile_api"),
    path("profile/", UsersListApiView.as_view(), name="profile_api"),
]
