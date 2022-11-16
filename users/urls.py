from django.urls import path
from .views import RegisterApiView, LoginApiView


urlpatterns = [path("signup/", RegisterApiView.as_view(), name="register_api"),
path("signin/", LoginApiView.as_view(), name="login_api")]
