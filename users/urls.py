from django.urls import path
from .views import RegisterApiView, LoginApiView, UserProfileView


urlpatterns = [
    path("signup/", RegisterApiView.as_view(), name="register_api"),
    path("signin/", LoginApiView.as_view(), name="login_api"),
    path("profile/<pk>/", UserProfileView.as_view(), name="profile_api")
]
